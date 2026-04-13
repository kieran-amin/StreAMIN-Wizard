# KieranWizard

Welcome to **KieranWizard** — a Kodi layout manager that installs and manages the StreAMIN build, including automated Real-Debrid and Trakt account authorization guidance.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Installing the Base Pack & Layout Pack](#installing-the-base-pack--layout-pack)
4. [Setup Checklist Screen](#setup-checklist-screen)
5. [Removing the Setup Screen Manually](#removing-the-setup-screen-manually)
6. [Updating Your Layout](#updating-your-layout)
7. [Troubleshooting](#troubleshooting)

---

## Requirements

Before you begin, make sure you have:

- **Kodi 21 (Nexus)** or later installed
- A **Real-Debrid** account — [realdebrid.com](https://real-debrid.com)
- A **Trakt** account — [trakt.tv](https://trakt.tv)
- An internet connection

---

## Installation

### Step 1 — Download the KieranWizard zip

1. On this GitHub page, click the green **`<> Code`** button near the top-right
2. Select **Download ZIP** from the dropdown
3. Save the file somewhere easy to find (e.g. your **Downloads** folder or a USB drive)

> 💡 **Do not unzip the file.** Kodi installs directly from the zip as downloaded.

---

### Step 2 — Enable Unknown Sources in Kodi

Kodi blocks zip installs by default. You only need to do this once:

1. Open Kodi → click the **⚙️ Settings** icon on the home screen
2. Go to **System** → **Add-ons**
3. Toggle **"Unknown sources"** to **ON**
4. Click **Yes** on the warning that appears

---

### Step 3 — Install the zip in Kodi

1. From the Kodi home screen, go to **Add-ons**
2. Click the **📦 open box icon** in the top-left corner
3. Select **Install from zip file**
4. Navigate to your **Downloads** folder (or wherever you saved the zip) and select **`plugin.program.kieranwizard-1.0.0.zip`**
5. Wait for the **"KieranWizard Add-on installed"** notification to appear in the top-right corner
6. **Restart Kodi** — the wizard will launch automatically on the next boot

---

## Installing the Base Pack & Layout Pack

The build is split into two packs that must be installed **in order**:

| Pack | What it installs | Install order |
|---|---|---|
| **Base Pack** | Core add-ons (Fen Light, TMDb Helper, etc.) | **First** |
| **Layout Pack** | Skin, home screen menus, shortcuts | **Second** |

### How to Install

1. Open the **KieranWizard** addon from your Kodi home screen or Add-ons menu
2. Select **Install Layout Pack**
3. Choose **Base Pack** → confirm the install and wait for it to complete
4. Once done, go back and choose **Layout Pack** → enter the passcode when prompted → confirm
5. Kodi will restart automatically after the Layout Pack installs
6. After the restart, the **Setup Checklist screen** will appear on your home screen

> ⚠️ **Important:** Always install the Base Pack before the Layout Pack. Installing out of order may cause missing add-ons or a broken home screen.

---

## Setup Checklist Screen

After the Layout Pack is installed, a **Setup Checklist** screen will appear as your home screen. This screen guides you through the three required authorization steps to get Real-Debrid and Trakt working.

**The screen will remain visible until you complete all steps and press Finalize.** This is intentional — it ensures you don't accidentally skip authorization.

### The 4 Items on the Checklist

Each item shows a ✓ (green) when complete or ✗ (red) when still pending.

---

#### Step 1: Initialize Debrid

This authorizes your **Real-Debrid** account inside **Fen Light**, which is the main streaming add-on.

1. Click **Step 1: Initialize Debrid** on the home screen
2. The **Fen Light settings** window will open automatically
3. Navigate to the **Accounts** or **Real-Debrid** section inside Fen Light settings
4. Select **Authorize Real-Debrid** and follow the on-screen instructions:
   - A code will be displayed — go to [real-debrid.com/device](https://real-debrid.com/device) on your phone or computer
   - Enter the code and click Authorize
5. Once the Kodi window closes, a dialog will ask **"Did you successfully authorize Real-Debrid?"**
6. Select **Yes** — the item will show a ✓ and be marked complete

> If you made a mistake or need to redo it, simply click the item again.

---

#### Step 2: Trakt 1 (Fen Light)

This authorizes your **Trakt** account inside **Fen Light** so it can track your watch history and sync your lists.

1. Click **Step 2: Trakt 1 (Fen Light)** on the home screen
2. The **Fen Light settings** window will open
3. Navigate to the **Trakt** section inside Fen Light settings
4. Select **Authorize Trakt** and follow the on-screen instructions:
   - A code will be displayed — go to [trakt.tv/activate](https://trakt.tv/activate) on your phone or computer
   - Enter the code and click Authorize
5. Once the window closes, confirm with **Yes** when asked
6. The item will show a ✓

---

#### Step 3: Trakt 2 (TMDb Helper)

This authorizes **Trakt** a second time inside **TMDb Helper**, which powers artwork, cast info, and recommendations. Both add-ons need their own separate Trakt authorization.

1. Click **Step 3: Trakt 2 (TMDb Helper)** on the home screen
2. The **TMDb Helper Trakt authorization** will launch directly (no settings window needed)
3. Follow the same steps as above — go to [trakt.tv/activate](https://trakt.tv/activate) and enter the displayed code
4. Confirm with **Yes** when asked
5. The item will show a ✓

---

#### Finalize Setup & Restart

Once all three steps show a ✓, click **Finalize Setup & Restart**.

- If any steps are still incomplete, you will be asked if you want to finish anyway — you can choose to skip and come back later
- When confirmed, the Setup screen will be **permanently disabled**
- Kodi will **restart automatically** to apply the changes
- After the restart, your normal home screen will load — the Setup screen will be gone

> The Setup screen will not come back on its own. If you need to re-run authorization (e.g. after a layout pack reinstall), see [Removing the Setup Screen Manually](#removing-the-setup-screen-manually) below.

---

## Removing the Setup Screen Manually

There are two ways to bring back or permanently dismiss the Setup screen outside of the normal flow.

---

### Method 1 — Via KieranWizard (Recommended)

1. From your home screen, navigate to the **KieranWizard** addon (or press your shortcut key)
2. Scroll down and select **Reset Setup Checklist**
3. All checkmarks will be cleared and the Setup screen will reappear on your home screen on the next skin reload

To **permanently dismiss** (hide the screen without completing setup):
1. Open **KieranWizard** → **Setup Checklist**
2. Click **Finalize Setup & Restart** — you will be given the option to finish even if steps are incomplete

---

### Method 2 — Via Kodi Skin Settings

The Setup screen visibility is controlled by a skin boolean called `SetupComplete`. You can toggle this manually:

1. In Kodi, go to **Settings** → **Interface** → **Skin**
2. Click **Configure skin...**
3. Look for a setting called **SetupComplete** or browse the boolean/toggle settings
4. **Enable** `SetupComplete` → the Setup screen will be hidden
5. **Disable** `SetupComplete` → the Setup screen will reappear

> Note: The exact location of skin settings depends on your installed skin. If you cannot find it in **Configure skin**, use Method 1 instead — it is more reliable.

---

### Method 3 — Via Kodi Debug Console (Advanced)

If you have access to a Kodi remote or debug interface, you can run this command directly:

**To hide the Setup screen:**
```
Skin.SetBool(SetupComplete)
```

**To show the Setup screen again:**
```
Skin.Reset(SetupComplete)
```

These can be entered via **Kodi's built-in keyboard shortcut** (if enabled) or through a remote control app that supports Kodi commands.

---

## Updating Your Layout

When a new Layout Pack version is released:

1. Open **KieranWizard** → **Install Layout Pack**
2. Select **Layout Pack** — if an update is available it will show an **[UPDATE]** badge
3. Install as normal — your saved data (Trakt, Debrid) will be preserved if you selected "Keep" during install
4. After the update, the Setup Checklist screen may reappear — this is by design, as new layout versions may require re-authorization

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Setup screen won't disappear after Finalize | Go to KieranWizard → Reset Setup Checklist → then re-run Finalize |
| Trakt not tracking plays | Repeat Step 2 or Step 3 — one of the authorizations may have expired |
| Real-Debrid links not working | Repeat Step 1 — your token may have expired. Re-authorize in Fen Light settings |
| Layout Pack install fails | Ensure Base Pack is installed first. Check your internet connection |
| Can't find KieranWizard in add-ons | Go to Add-ons → My add-ons → Program add-ons → KieranWizard |
| Setup Checklist screen missing | It was completed. Use Method 2 or 3 above to reset it if needed |
