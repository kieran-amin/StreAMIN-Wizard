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
# IMPORTANT: These names must exactly match the skin setting IDs shipped in the
# Layout Pack (case-sensitive). The Layout Pack uses lowercase IDs.
SKIN_BOOL_TRAKT_TMDB = 'setup_trakt_tmdb_authorized'      # Step 1: TMDb Helper
SKIN_BOOL_SUBTITLES  = 'setup_subtitles_configured'       # Step 2: Subtitles (a4kSubtitles)
SKIN_BOOL_RD = 'setup_rd_authorized'                      # Step 3: Fen Light (Real-Debrid)
SKIN_BOOL_TRAKT_FENLIGHT = 'setup_trakt_fenlight_authorized'  # Step 3: Fen Light (Trakt)
SKIN_BOOL_SETUP_COMPLETE = 'setupcomplete'


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
        First waits up to 10 seconds for an auth window to appear, then waits
        for the user to close it.
        """
        # 1. Wait dynamically up to 10 seconds for an auth window to appear
        window_appeared = False
        for _ in range(20):  # 20 * 500ms = 10 seconds
            any_window_active = (
                xbmc.getCondVisibility('Window.IsVisible(addonsettings)') or
                xbmc.getCondVisibility('Window.IsVisible(yesnodialog)') or
                xbmc.getCondVisibility('Window.IsVisible(okdialog)') or
                xbmc.getCondVisibility('Window.IsVisible(progressdialog)') or
                xbmc.getCondVisibility('Window.IsVisible(virtualkeyboard)')
            )
            if any_window_active:
                window_appeared = True
                break
            xbmc.sleep(500)
            
        if not window_appeared:
            # If no window spawned after 10 full seconds, proceed anyway
            return

        # 2. Once a window has appeared, wait for it (up to 10 mins) to close
        max_checks = 1200  # 10 minutes
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

        # Brief settle time for the UI backing out
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
    #  Homescreen checklist item comments:
    #
    #  Checklist order:
    #    Step 1 — TMDb Helper   (Trakt + OMDb key)
    #    Step 2 — Subtitles     (a4kSubtitles — optional)
    #    Step 3 — Fen Light     (Trakt + Real-Debrid + OMDb key)
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

    def open_tmdb_settings(self):
        """Open TMDb Helper settings so the user can set Trakt + OMDb keys."""
        return self._run_auth(
            'Addon.OpenSettings(plugin.video.themoviedb.helper)',
            'plugin.video.themoviedb.helper',
            'TMDb Helper Settings'
        )

    def open_subtitles_settings(self):
        """Open a4kSubtitles settings so the user can configure subtitles."""
        return self._run_auth(
            'Addon.OpenSettings(service.subtitles.a4ksubtitles)',
            'service.subtitles.a4ksubtitles',
            'a4kSubtitles Settings'
        )

    def open_fenlight_settings(self):
        """Open Fen Light settings so the user can set Trakt, RD, and OMDb keys."""
        return self._run_auth(
            'Addon.OpenSettings(plugin.video.fenlight)',
            'plugin.video.fenlight',
            'Fen Light Settings'
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

    def checklist_tmdb_settings(self):
        """Homescreen checklist: Open TMDb Helper settings (Step 1)."""
        launched = self.open_tmdb_settings()
        if launched:
            self._confirm_and_set_bool('TMDb Helper (Trakt + OMDb key)', SKIN_BOOL_TRAKT_TMDB)

    def checklist_subtitles(self):
        """Homescreen checklist: Open a4kSubtitles settings (Step 2 — optional)."""
        if not self._addon_installed('service.subtitles.a4ksubtitles'):
            # Subtitles addon not installed — skip gracefully and mark done
            self.dialog.ok(
                CONFIG.ADDONTITLE,
                "[COLOR {0}]Subtitles addon not found.[CR][CR]"
                "[COLOR {1}]a4kSubtitles is not installed in this build.[CR]"
                "Skipping this step.[/COLOR]".format(CONFIG.COLOR1, CONFIG.COLOR2))
            xbmc.executebuiltin('Skin.SetBool({})'.format(SKIN_BOOL_SUBTITLES))
            return
        launched = self.open_subtitles_settings()
        if launched:
            self._confirm_and_set_bool('Subtitles (a4kSubtitles)', SKIN_BOOL_SUBTITLES)

    def checklist_fenlight_settings(self):
        """Homescreen checklist: Open Fen Light settings (Step 3)."""
        launched = self.open_fenlight_settings()
        if launched:
            # Fen Light covers both RD and Trakt — confirm once and mark both bools
            success = self._confirm_and_set_bool('Fen Light (Trakt + Real-Debrid + OMDb)', SKIN_BOOL_RD)
            if success:
                xbmc.executebuiltin('Skin.SetBool({})'.format(SKIN_BOOL_TRAKT_FENLIGHT))

    def checklist_finish(self):
        """
        Mark setup as complete. Sets Skin.Bool(SetupComplete) which the skin
        uses to hide the Setup page from the homescreen.

        We use ReloadSkin() instead of RestartApp() so that:
          1. The setup panel hides immediately without a full Kodi restart.
          2. The skin lands on whatever its default first-visible home panel is
             (KStreams), rather than the now-gone setup panel.

        Skin.SetBool is session-only; startup.py re-applies all bools on
        every boot using the persisted 'setup_complete' addon setting.
        """
        # Check if all items have been marked as complete
        all_done = (
            xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_TRAKT_TMDB)) and
            xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_SUBTITLES)) and
            xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_RD))
        )

        if not all_done:
            proceed = self.dialog.yesno(
                CONFIG.ADDONTITLE,
                "[COLOR {0}]Not all steps have been completed yet.[CR][CR]"
                "Are you sure you want to finish setup?[/COLOR]".format(CONFIG.COLOR2),
                yeslabel='[B]Yes, Finish Anyway[/B]',
                nolabel='[B]Go Back[/B]')
            if not proceed:
                return

        # Set the skin bool for this session
        xbmc.executebuiltin('Skin.SetBool({})'.format(SKIN_BOOL_SETUP_COMPLETE))

        # Persist to addon settings so the bool is re-applied after every restart
        CONFIG.set_setting('setup_complete', 'true')

        logging.log("[Checklist] Setup marked as complete (persisted to addon settings)",
                    level=xbmc.LOGINFO)

        self.dialog.ok(
            CONFIG.ADDONTITLE,
            "[COLOR {0}][B]Setup Complete![/B][/COLOR][CR][CR]"
            "[COLOR {1}]The Setup screen is now hidden.[CR]"
            "Returning to your home screen — navigate to KStreams.[/COLOR]".format(
                CONFIG.COLOR1, CONFIG.COLOR2))

        # Reload the skin in-place so the setup panel hides immediately.
        # This avoids a full Kodi restart which would land on the wrong home panel.
        xbmc.executebuiltin('ReloadSkin()')

    def checklist_reset(self):
        """
        Reset the checklist: clears all Skin.Bools so the Setup page
        reappears and all items show as incomplete.
        Also clears the persistent addon setting so startup.py no longer
        re-applies SetupComplete on boot.
        Useful for re-running setup or after a layout pack update.
        """
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_TRAKT_TMDB))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_SUBTITLES))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_RD))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_TRAKT_FENLIGHT))
        xbmc.executebuiltin('Skin.Reset({})'.format(SKIN_BOOL_SETUP_COMPLETE))

        # Also clear the persistent flag so the skin bool isn't re-applied on next boot
        CONFIG.set_setting('setup_complete', 'false')

        logging.log("[Checklist] All skin bools reset (addon setting cleared)", level=xbmc.LOGINFO)
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
        Each item is clickable and opens the relevant addon's settings.
        Shows ✓/✗ status based on Skin.Bool values.

        Order:
          1. TMDb Helper  — set Trakt + OMDb API key
          2. Subtitles    — configure a4kSubtitles (optional)
          3. Fen Light    — set Trakt, Real-Debrid, and OMDb key
        """
        logging.log("[Checklist Widget] Generating checklist listing", level=xbmc.LOGINFO)
        from resources.libs.common import directory

        # Check completion status via skin bools
        tmdb_done     = xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_TRAKT_TMDB))
        subs_done     = xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_SUBTITLES))
        fenlight_done = xbmc.getCondVisibility('Skin.HasSetting({})'.format(SKIN_BOOL_RD))

        # Status indicators
        done = '[COLOR limegreen]\u2713[/COLOR]'  # ✓
        todo = '[COLOR red]\u2717[/COLOR]'         # ✗

        # Step 1: TMDb Helper
        directory.add_file(
            '{0}  [B]Step 1:[/B] TMDb Helper — Trakt + OMDb Key'.format(done if tmdb_done else todo),
            {'mode': 'accounts', 'action': 'checklist_tmdb_settings'},
            icon=CONFIG.ICONTRAKT,
            description='Open TMDb Helper settings to enter your Trakt and OMDb API keys. See README for exact steps.')

        # Step 2: Subtitles
        directory.add_file(
            '{0}  [B]Step 2:[/B] Subtitles (Optional)'.format(done if subs_done else todo),
            {'mode': 'accounts', 'action': 'checklist_subtitles'},
            icon=CONFIG.ICONSETTINGS,
            description='Open a4kSubtitles settings to configure subtitle providers. Optional — skip if not needed.')

        # Step 3: Fen Light
        directory.add_file(
            '{0}  [B]Step 3:[/B] Fen Light — Trakt + Real-Debrid + OMDb'.format(done if fenlight_done else todo),
            {'mode': 'accounts', 'action': 'checklist_fenlight_settings'},
            icon=CONFIG.ICONDEBRID,
            description='Open Fen Light settings to authorize Trakt, Real-Debrid, and OMDb. See README for exact steps.')

        directory.add_separator()

        directory.add_file(
            '[B][COLOR gold]>> Finish Setup <<[/COLOR][/B]',
            {'mode': 'accounts', 'action': 'checklist_finish'},
            icon=CONFIG.ICONSETTINGS,
            description='Hide this setup screen and return to your home screen.')

        logging.log("[Checklist Widget] Listing successfully generated", level=xbmc.LOGINFO)

    # ==========================================================================
    #  Popup loop (original post-install flow, still used from startup.py)
    # ==========================================================================

    def post_install_loop(self):
        """
        Show a persistent setup menu as a popup. After each auth attempt,
        the menu reappears with a checkmark on completed items. The menu
        only closes when the user selects 'Done' or presses Back.

        Order matches the homescreen checklist: TMDb → Subtitles → Fen Light.
        """
        logging.log("[Post Install Setup] Starting post-install loop", level=xbmc.LOGINFO)
        self.completed = set()

        labels = [
            'Configure TMDb Helper (Trakt + OMDb)',
            'Configure Subtitles (a4kSubtitles — optional)',
            'Configure Fen Light (Trakt + Real-Debrid + OMDb)',
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
                self.open_tmdb_settings()
                self.completed.add(0)
            elif ret == 1:
                self.open_subtitles_settings()
                self.completed.add(1)
            elif ret == 2:
                self.open_fenlight_settings()
                self.completed.add(2)
            elif ret == 3 or ret == -1:
                break

        logging.log("[Post Install Setup] Completed", level=xbmc.LOGINFO)
        self.dialog.ok(CONFIG.ADDONTITLE,
            "[COLOR {0}][B]Setup Complete![/B][/COLOR][CR][CR]"
            "[COLOR {1}]You are now ready to use Kodi.[/COLOR]".format(
                CONFIG.COLOR1, CONFIG.COLOR2))
