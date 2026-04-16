# StreAMIN Wizard — Beta Install Guide

> **Beta note:** This build is distributed as a ZIP file — no GitHub repository required. Follow the steps below carefully.

---

## What You Need Before Starting

| Service | Free? | Why |
|---|---|---|
| [Trakt.tv](https://trakt.tv) account | ✅ Free | Tracks your watch history. Required by TMDb Helper & Fen Light |
| [Real-Debrid](https://real-debrid.com) subscription | 💳 Paid | Unlocks high-quality streams. Required by Fen Light |
| [OMDb API key](https://www.omdbapi.com/apikey.aspx) | ✅ Free tier | Metadata lookups. Used by TMDb Helper & Fen Light |

---

## Step 1 — Install the Wizard

1. **Download** `plugin.program.kieranwizard.zip` (provided by Kieran).
2. In Kodi, go to **Settings → Add-ons → Install from zip file**.
3. Navigate to where you saved the ZIP and select it.
4. Wait for the *"Add-on installed"* notification.
5. *(If Kodi asks about unknown sources, enable them in Settings → System → Add-ons.)*

---

## Step 2 — Install the StreAMIN Build

1. Go to **Add-ons → Program Add-ons → KieranWizard**.
2. Select **Builds** from the wizard menu.
3. Choose **StreAMIN** and select **Fresh Install**.
4. When prompted to save data, choose as appropriate and confirm.
5. Kodi will restart automatically with the new skin applied.

---

## Step 3 — Complete the Setup Checklist

After the build installs and Kodi restarts, you will see a **Setup Checklist** on your home screen. Work through each step:

---

### Step 1 of 3 — TMDb Helper

**Click the TMDb Helper item** on the checklist. This opens TMDb Helper settings.

Navigate to these tabs and enter your keys:

| Tab | Setting | Value |
|---|---|---|
| **Trakt** | Authorize Trakt | Click **Authorize** and follow the on-screen code |
| **APIs** | OMDb API | Paste your free OMDb API key |

Close settings when done, then click **Yes** to mark this step complete.

---

### Step 2 of 3 — Subtitles *(Optional)*

**Click the Subtitles item** to open a4kSubtitles settings.

- If you want subtitles: select your preferred providers (e.g. OpenSubtitles) and log in.
- If you don't need subtitles: click the item and select **Yes** to skip and mark it done.

---

### Step 3 of 3 — Fen Light

**Click the Fen Light item** to open Fen Light settings.

Navigate to these tabs and enter your keys:

| Tab | Setting | Value |
|---|---|---|
| **Trakt** | Authorise Trakt | Click **Authorise** and follow the on-screen code |
| **Debrid** | Real-Debrid | Click **Authorise** and follow the on-screen code |
| **APIs** | OMDb API | Paste your free OMDb API key |

Close settings when done, then click **Yes** to mark this step complete.

---

### Finish Setup

Once all three steps show a green ✓, click **>> Finish Setup <<**.  
The setup screen will hide and your home screen will return to the KStreams page.

---

## Keyboard Shortcuts (PC)

| Key | Action |
|---|---|
| `Backspace` | Go back |
| `C` | Context menu |
| `I` | Info / details |
| `X` | Stop playback |
| `Space` | Pause / resume |
| `F` | Fast forward |
| `R` | Rewind |

---

## Troubleshooting

**Setup checklist reappears after restart?**  
The checklist hides based on a skin bool that is re-applied on every Kodi startup. If it keeps showing, open the wizard → go to the Setup Checklist → click **Finish Setup** again.

**Build prompt appears every time?**
This means the build URL in `builds.txt` is not reachable. Contact Kieran — the file hosting link may need updating.

**Can't find a stream / Real-Debrid not working?**
Make sure Real-Debrid is authorized in Fen Light (Step 3 above). You can re-open Fen Light settings at any time via **Add-ons → Video Add-ons → Fen Light**.
