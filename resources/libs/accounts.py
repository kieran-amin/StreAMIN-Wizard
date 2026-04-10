import sys
import xbmc
import xbmcgui
import os

import sqlite3
import datetime

from resources.libs.common import logging
from resources.libs.common import tools
from resources.libs.common.config import CONFIG

# Skin bool names used for the homescreen checklist page.
# These persist in the skin's settings and survive Kodi restarts.
SKIN_BOOL_RD = 'Setup_RD_Authorized'
SKIN_BOOL_TRAKT_FENLIGHT = 'Setup_Trakt_FenLight_Authorized'
SKIN_BOOL_TRAKT_TMDB = 'Setup_Trakt_TMDb_Authorized'
SKIN_BOOL_SETUP_COMPLETE = 'SetupComplete'


class Accounts:

    def __init__(self):
        self.dialog = xbmcgui.Dialog()
        self.completed = set()  # Track which items the user completed this session

    def _addon_installed(self, addon_id):
        """Check if an addon is installed by verifying its directory exists."""
        return os.path.exists(os.path.join(CONFIG.ADDONS, addon_id))

    def _wait_for_window_close(self):
        """
        Wait for any auth-related windows (addon settings, dialogs, etc.) to close.
        Polls every 500ms, max 10 minutes. This keeps the Python thread busy
        so the dialog.select loop doesn't resume while the user is still
        interacting with the auth window.
        """
        # Give the window time to actually open first
        xbmc.sleep(2000)

        max_checks = 1200  # 10 minutes (1200 * 500ms)
        for _ in range(max_checks):
            any_window_active = (
                xbmc.getCondVisibility('Window.IsVisible(addonsettings)') or
                xbmc.getCondVisibility('Window.IsVisible(yesnodialog)') or
                xbmc.getCondVisibility('Window.IsVisible(okdialog)') or
                xbmc.getCondVisibility('Window.IsVisible(progressdialog)') or
                xbmc.getCondVisibility('Window.IsVisible(virtualkeyboard)')
            )
            if not any_window_active:
                break
            xbmc.sleep(500)

        # Brief settle time for the UI
        xbmc.sleep(500)

    def _run_auth(self, auth_command, addon_id, service_name):
        """
        Launch an authorization command and wait for the user to finish.
        Returns True if the addon was found and the command was launched,
        False if the addon is missing.
        """
        if not self._addon_installed(addon_id):
            self.dialog.ok(CONFIG.ADDONTITLE,
                "[COLOR red]Addon Not Installed[/COLOR][CR][CR]"
                "[COLOR {0}]{1} is not installed.[CR]"
                "Please install it first.[/COLOR]".format(CONFIG.COLOR2, addon_id))
            return False

        logging.log("[Post Install Setup] Launching: {}".format(service_name))
        xbmc.executebuiltin(auth_command)
        self._wait_for_window_close()
        logging.log("[Post Install Setup] Returned from: {}".format(service_name))
        return True

    # ==========================================================================
    #  Core auth actions (used by both popup loop and homescreen checklist)
    # ==========================================================================

    def fenlight_rd(self):
        """Authorize Real-Debrid for Fen Light."""
        return self._run_auth(
            'Addon.OpenSettings(plugin.video.fenlight)',
            'plugin.video.fenlight',
            'Real-Debrid (Fen Light)'
        )

    def fenlight_trakt(self):
        """Authorize Trakt for Fen Light."""
        return self._run_auth(
            'Addon.OpenSettings(plugin.video.fenlight)',
            'plugin.video.fenlight',
            'Trakt (Fen Light)'
        )

    def tmdb_trakt(self):
        """Authorize Trakt for TMDbHelper using its direct auth deep-link."""
        return self._run_auth(
            'RunScript(plugin.video.themoviedb.helper, authenticate_trakt)',
            'plugin.video.themoviedb.helper',
            'Trakt (TMDbHelper)'
        )

    # ==========================================================================
    #  Homescreen checklist actions (called via RunPlugin from skin shortcuts)
    #
    #  Each action:
    #    1. Opens the addon settings / runs the auth command
    #    2. Waits for the user to finish
    #    3. Asks "Did you successfully authorize?"
    #    4. If yes -> sets a Skin.Bool so the skin can show a checkmark
    #
    #  RunPlugin commands for skin shortcuts:
    #    RunPlugin(plugin://plugin.program.kieranwizard/?mode=accounts&action=checklist_fenlight_rd)
    #    RunPlugin(plugin://plugin.program.kieranwizard/?mode=accounts&action=checklist_fenlight_trakt)
    #    RunPlugin(plugin://plugin.program.kieranwizard/?mode=accounts&action=checklist_tmdb_trakt)
    #    RunPlugin(plugin://plugin.program.kieranwizard/?mode=accounts&action=checklist_finish)
    # ==========================================================================

    def _confirm_and_set_bool(self, service_name, skin_bool):
        """
        Ask the user if they successfully authorized, and set the
        corresponding Skin.Bool if they confirm.
        """
        success = self.dialog.yesno(
            CONFIG.ADDONTITLE,
            "[COLOR {0}]Did you successfully authorize "
            "[COLOR {1}]{2}[/COLOR]?[/COLOR]".format(
                CONFIG.COLOR2, CONFIG.COLOR1, service_name),
            yeslabel='[B][COLOR limegreen]Yes[/COLOR][/B]',
            nolabel='[B][COLOR red]Not Yet[/COLOR][/B]')

        if success:
            xbmc.executebuiltin('Skin.SetBool({})'.format(skin_bool))
            logging.log_notify(
                CONFIG.ADDONTITLE,
                "[COLOR limegreen]{} Authorized[/COLOR]".format(service_name))
            logging.log("[Checklist] {} -> authorized (Skin.Bool set)".format(
                skin_bool), level=xbmc.LOGINFO)
        else:
            logging.log_notify(
                CONFIG.ADDONTITLE,
                "[COLOR red]{} Not Authorized[/COLOR]".format(service_name))

        return success

    def checklist_fenlight_rd(self):
        """Homescreen checklist: Authorize Real-Debrid in Fen Light."""
        launched = self.fenlight_rd()
        if launched:
            self._confirm_and_set_bool('Real-Debrid', SKIN_BOOL_RD)

    def checklist_fenlight_trakt(self):
        """Homescreen checklist: Authorize Trakt in Fen Light."""
        launched = self.fenlight_trakt()
        if launched:
            self._confirm_and_set_bool('Trakt (Fen Light)', SKIN_BOOL_TRAKT_FENLIGHT)

    def checklist_tmdb_trakt(self):
        """Homescreen checklist: Authorize Trakt in TMDb Helper."""
        launched = self.tmdb_trakt()
        if launched:
            self._confirm_and_set_bool('Trakt (TMDb)', SKIN_BOOL_TRAKT_TMDB)

    def checklist_finish(self):
        """
        Mark setup as complete. Sets Skin.Bool(SetupComplete) which the skin
        uses to hide the Setup page from the homescreen.
        """
        # Check if all items have been marked as authorized
        all_done = (
            xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_RD)) and
            xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_TRAKT_FENLIGHT)) and
            xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_TRAKT_TMDB))
        )

        if not all_done:
            proceed = self.dialog.yesno(
                CONFIG.ADDONTITLE,
                "[COLOR {0}]Not all services have been authorized yet.[CR][CR]"
                "Are you sure you want to finish setup?[/COLOR]".format(CONFIG.COLOR2),
                yeslabel='[B]Yes, Finish Anyway[/B]',
                nolabel='[B]Go Back[/B]')
            if not proceed:
                return

        xbmc.executebuiltin('Skin.SetBool({})'.format(SKIN_BOOL_SETUP_COMPLETE))
        logging.log("[Checklist] Setup marked as complete", level=xbmc.LOGINFO)

        self.dialog.ok(
            CONFIG.ADDONTITLE,
            "[COLOR {0}][B]Setup Complete![/B][/COLOR][CR][CR]"
            "[COLOR {1}]The Setup screen has been disabled.[CR]"
            "Kodi will now restart to apply changes.[/COLOR]".format(
                CONFIG.COLOR1, CONFIG.COLOR2))

        # Restart Kodi so the Setup screen disappears and all changes apply.
        # sys.exit() immediately releases the plugin thread — without it, Kodi
        # deadlocks waiting for this RunPlugin to finish before it can restart.
        xbmc.executebuiltin('RestartApp()')
        sys.exit()

    def checklist_reset(self):
        """
        Reset the checklist: clears all Skin.Bools so the Setup page
        reappears and all items show as incomplete.
        Useful for re-running setup or after a layout pack update.
        """
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_RD))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_TRAKT_FENLIGHT))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_TRAKT_TMDB))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_SETUP_COMPLETE))

        logging.log("[Checklist] All skin bools reset", level=xbmc.LOGINFO)
        logging.log_notify(
            CONFIG.ADDONTITLE,
            "[COLOR limegreen]Setup Checklist Reset[/COLOR]")

    # ==========================================================================
    #  Widget-compatible directory listing
    #
    #  Use this as a widget source path in your skin:
    #    plugin://plugin.program.kieranwizard/?mode=checklist
    #
    #  It returns a clickable list of checklist items with ✓/✗ indicators.
    # ==========================================================================

    def get_checklist_listing(self):
        """
        Return a Kodi directory listing for the homescreen widget.
        Each item is clickable and triggers the corresponding auth flow.
        Shows ✓/✗ status based on Skin.Bool values.
        """
        logging.log("[Checklist Widget] Generating checklist listing", level=xbmc.LOGINFO)
        from resources.libs.common import directory

        # Check completion status via skin bools
        rd_done = xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_RD))
        trakt_fl_done = xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_TRAKT_FENLIGHT))
        trakt_tmdb_done = xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_TRAKT_TMDB))

        # Status indicators
        done = '[COLOR limegreen]\u2713[/COLOR]'    # ✓
        todo = '[COLOR red]\u2717[/COLOR]'           # ✗

        # Auth items with status
        directory.add_file(
            '{0}  Authorize Real-Debrid'.format(done if rd_done else todo),
            {'mode': 'accounts', 'action': 'checklist_fenlight_rd'},
            icon=CONFIG.ICONDEBRID,
            description='Open Fen Light settings to authorize your Real-Debrid account.')

        directory.add_file(
            '{0}  Authorize Trakt (Fen Light)'.format(done if trakt_fl_done else todo),
            {'mode': 'accounts', 'action': 'checklist_fenlight_trakt'},
            icon=CONFIG.ICONTRAKT,
            description='Open Fen Light settings to authorize your Trakt account.')

        directory.add_file(
            '{0}  Authorize Trakt (TMDb)'.format(done if trakt_tmdb_done else todo),
            {'mode': 'accounts', 'action': 'checklist_tmdb_trakt'},
            icon=CONFIG.ICONTRAKT,
            description='Authorize Trakt directly in TMDb Helper.')

        directory.add_separator()

        directory.add_file(
            '[B][COLOR gold]>> Finish Setup & Restart <<[/COLOR][/B]',
            {'mode': 'accounts', 'action': 'checklist_finish'},
            icon=CONFIG.ICONSETTINGS,
            description='Disable this setup screen and restart Kodi.')

        logging.log("[Checklist Widget] Listing successfully generated", level=xbmc.LOGINFO)

    # ==========================================================================
    #  Popup loop (original post-install flow, still used from startup.py)
    # ==========================================================================

    def post_install_loop(self):
        """
        Show a persistent setup menu as a popup. After each auth attempt,
        the menu reappears with a checkmark on completed items. The menu
        only closes when the user selects 'Done' or presses Back.
        """
        logging.log("[Post Install Setup] Starting post-install loop", level=xbmc.LOGINFO)
        self.completed = set()

        labels = [
            'Authorize Real-Debrid (Fen Light)',
            'Authorize Trakt (Fen Light)',
            'Authorize Trakt (TMDbHelper)',
        ]

        while True:
            # Build menu options with completion status
            options = []
            for i, label in enumerate(labels):
                if i in self.completed:
                    options.append('[COLOR limegreen]\u2713[/COLOR]  {}'.format(label))
                else:
                    options.append('[COLOR red]\u2717[/COLOR]  {}'.format(label))
            options.append('[B][COLOR limegreen]>> Done / Continue <<[/COLOR][/B]')

            ret = self.dialog.select(
                CONFIG.ADDONTITLE + '  -  Post Install Setup', options)

            if ret == 0:
                self.fenlight_rd()
                self.completed.add(0)
            elif ret == 1:
                self.fenlight_trakt()
                self.completed.add(1)
            elif ret == 2:
                self.tmdb_trakt()
                self.completed.add(2)
            elif ret == 3 or ret == -1:
                break

        logging.log("[Post Install Setup] Completed", level=xbmc.LOGINFO)
        self.dialog.ok(CONFIG.ADDONTITLE,
            "[COLOR {0}][B]Setup Complete![/B][/COLOR][CR][CR]"
            "[COLOR {1}]You are now ready to use Kodi.[/COLOR]".format(
                CONFIG.COLOR1, CONFIG.COLOR2))
