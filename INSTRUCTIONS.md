# KieranWizard Tutorial

Welcome to the official tutorial for KieranWizard! This guide will walk you through everything you need to know—from installation to advanced tips and tricks.

## ⚠️ READ THIS FIRST — Common Questions & Rules

> **Stop.** Read this entire section before texting/calling me. If you call me and I can tell it's your first time reading these instructions, I will come find you.

1. **Why do I need Real-Debrid?**
   Real-Debrid is a multi-hoster caching service. It caches data on its high-speed servers and provides direct access — meaning you access content from their secure servers rather than via public peer networks. It also acts as an encrypted layer so your connection is protected. TLDR: You can stream content without getting caught. 

2. **Each person MUST have their own Real-Debrid account.**
   > ⚠️ **DO NOT share a Real-Debrid account with anyone, even within the same household or city.** Real-Debrid actively monitors for account sharing. If two people use the same account from different IPs (even in the same city), your account **WILL be permanently banned** with no refund. I learned this the hard way. Buy your own subscription — it's like $4/month. This is non-negotiable.

3. **Why is my stream buffering?**
   Streaming = downloading in real time. If it buffers, your internet is too slow for the file size you picked. Pick a smaller file or check your connection.

4. **For now, use only on laptop.** I will provide Firestick instructions later (they suck) and Onn 4K Pro instructions (which is good).

5. **Do NOT call me with questions about Trakt or Real-Debrid setup.** These are straightforward services with their own help pages. Google it. I will help with issues with the build itself.

---

## 📋 Table of Contents
- [Prerequisites & Accounts Needed](#prerequisites--accounts-needed)
- [Real-Debrid Setup](#real-debrid-setup)
- [Installation](#installation)
  - [Step 1: Install Kodi](#step-1-install-kodi)
  - [Step 2: Enable Unknown Sources](#step-2-enable-unknown-sources)
  - [Step 3: Download the Wizard](#step-3-download-the-wizard)
  - [Step 4: Install the Wizard from Zip File](#step-4-install-the-wizard-from-zip-file)
  - [Step 5: Install the Base Pack](#step-5-install-the-base-pack)
  - [Step 6: Install the Layout Pack](#step-6-install-the-layout-pack)
  - [Step 7: Authorize Your Accounts](#step-7-authorize-your-accounts)
- [Setting up Addons](#setting-up-addons)
- [How to Use](#how-to-use)
- [Anime Configuration](#anime-configuration)
- [Tips & Tricks](#tips--tricks)
- [Troubleshooting](#troubleshooting)

---

## 🔑 Prerequisites & Accounts Needed
Before you begin, ensure you have the following accounts and software ready. The first two are **required** — the rest are strongly recommended.

### Required Accounts
1.  **Real-Debrid**
    *   *Why?* For high-quality, buffer-free media access. **This is required — nothing works without it.**
    *   *Sign up:* [https://real-debrid.com/?id=9373068](https://real-debrid.com/?id=9373068)
    *   ⚠️ **You MUST have your own account. Do NOT share with anyone. Account sharing = permanent ban.**
    *   *Cost:* ~$4/month (180-day plan is best value)

2.  **Trakt.tv**
    *   *Why?* To sync your watch history and get personalized recommendations.
    *   *Sign up:* [https://trakt.tv](https://trakt.tv)
    *   *Download the Trakt app on your phone as well*

### Recommended Accounts
3.  **Opensubtitles.org**
    *   *Why?* For subtitles.
    *   *Sign up:* [https://opensubtitles.org](https://opensubtitles.org)
    *   *Create a free account and remember your credentials. You'll type them into addon settings.*

4.  **OMDB API**
    *   *Why?* For movie and TV show information and ratings from sources such as IMDb, Rotten Tomatoes and displays awards received.
    *   *Sign up:* [https://www.omdbapi.com](https://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0MXBaUo2PpHbEmO0KsvHCBMiAqbwPSispxmMnBH5rXb8%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAV6O6wfBwA%2F81aWW2BYfVtumSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulGztfcyzE1Lkxwo9dYYBItHiFDZeQhYzawd9QWEG%2BI9i&at=freeAcct&Email=)
    *   *Request a free API key. Set the use as "personal media hub."*

5.  **MyAnimeList** *(only if you watch anime)*
    *   *Why?* To sync your anime watch history and lists.
    *   *Sign up:* [https://myanimelist.net](https://myanimelist.net)
    *   *Download the MAL app on your phone as well*

---

## 🔗 Real-Debrid Setup

Real-Debrid is essential for high-speed streaming. Set up your account **before** installing the build so you're ready to authorize when prompted.

> ⚠️ **REMINDER: Each person needs their OWN Real-Debrid account. Sharing an account (even within the same city) WILL get your account permanently banned. Each account provides one stream at a time.**

1. **Sign up for Real-Debrid**
    *   Go to [https://real-debrid.com](https://real-debrid.com/?id=9373068)
    *   Sign up for an account.
    *   Click this link after verifying your account to purchase premium: [http://real-debrid.com/?id=9373068](https://real-debrid.com/?id=9373068). This is my affiliate link which gets you a cheaper price. **Buy the 180-day option for best value.**
    *   To pay, I use an app on my phone called **Privacy** to generate a virtual card. This app is safe and trusted — I've used it for years. Set up a temporary card, limit it to $20.
    *   Ensure you have premium by checking your account on the website. It will say "premium:" with the duration remaining (e.g., 180 days).

2. **How Authorization Works (When Prompted Later)**
    *   A code will appear on your Kodi screen (e.g., `AB12-CD34`).
    *   On your phone or computer, go to [https://real-debrid.com/device](https://real-debrid.com/device).
    *   Log in if needed and enter the code displayed on your TV/screen.
    *   Once authorized, you will see a confirmation. You can now stream with premium links.

---

## 🚀 Installation

Follow these steps **in order**. The build installs in two parts: a **Base Pack** (core addons) and a **Layout Pack** (skin and menus). Do not skip steps.

### Step 1: Install Kodi

1.  Download **Kodi 21 Omega** from [https://kodi.tv/download](https://kodi.tv/download).
2.  Choose the correct version for your operating system (Windows, macOS, Android, etc.).
3.  Run the installer and follow the on-screen prompts.
4.  Launch Kodi once and let it finish its initial setup. You should see the default Kodi home screen (Estuary skin).

### Step 2: Enable Unknown Sources

Kodi blocks third-party add-on installations by default. You must enable "Unknown Sources" to install the wizard.

1.  From the Kodi home screen, click the **gear icon** ⚙️ (top-left) to open **Settings**.
2.  Click **System**.
3.  On the left sidebar, click **Add-ons**.
4.  > ⚠️ **Important:** If you don't see the "Add-ons" option in System settings, you may need to change the settings level. In the bottom-left corner of the Settings page, click the gear icon until it says **"Advanced"** or **"Expert"**.
5.  Toggle **"Unknown sources"** to **ON**.
6.  A warning popup will appear — click **Yes** to confirm.
7.  Press **Esc** or **Back** to return to the home screen.


### Step 3: Download the Wizard

1.  Go to the KieranWizard GitHub page: [https://github.com/kieran-amin/plugin.program.kieranwizard](https://github.com/kieran-amin/plugin.program.kieranwizard)
2.  Click the green **`<> Code`** button near the top-right of the page.
3.  Select **"Download ZIP"** from the dropdown.
4.  Your browser will download a file called **`plugin.program.kieranwizard-main.zip`**.
5.  **Do not unzip it.** Kodi installs directly from the `.zip` file.
6.  Move or note where the file saved — by default it goes to your **Downloads** folder.

> 💡 **Tip:** Rename the file to something shorter like `kieranwizard.zip` if you like — it doesn't matter what it's called.

---

### Step 4: Install the Wizard from Zip File

1.  From the Kodi home screen, click **Add-ons** in the left sidebar.
2.  Click the **open box icon** 📦 in the top-left corner — this opens the Add-on browser.
3.  Select **"Install from zip file"**.
4.  If a popup about Unknown Sources appears, click **Settings** and enable it (see Step 2), then come back.
5.  A file browser will open. Navigate to your **Downloads** folder:

#### 🖥️ Windows
- In the file browser, scroll up and look for **`Home folder`** (or your username, e.g. `C:\Users\YourName`).
- Open it, then open the **`Downloads`** folder.
- Find and click **`plugin.program.kieranwizard-main.zip`**.

> ⚠️ **Can't find your Downloads folder?** Kodi's file browser starts in its own folder. Keep scrolling up past `Root filesystem` until you see your user folders, or look under **`Windows`** → **`C:`** → **`Users`** → **`(your username)`** → **`Downloads`**.

#### 📱 Android / Firestick
- Look for **`Internal Storage`** or **`sdcard`** in the file browser.
- Open it and navigate to the **`Download`** folder.
- Find and click the zip file.

#### 💾 USB Drive
- Plug in your USB drive before opening Kodi.
- In the file browser, it will appear as a separate removable storage option.
- Navigate to it and select the zip file.

6.  Wait for the **"KieranWizard Add-on installed"** notification to appear in the top-right corner. This may take 10-20 seconds.

### Step 5: Install the Base Pack

The Base Pack installs all the core addons and settings. **You must install this first.**

1.  After the wizard is installed, **restart Kodi** — close it completely and reopen it.
2.  The wizard will launch automatically and show a build prompt. Click **"Build Menu"**.
    *   If the prompt doesn't appear, go to **Add-ons** → **Program add-ons** → **KieranWizard** manually.
3.  Select **"Base Pack"** from the list.
4.  Click **"Fresh Install"**.
5.  Confirm by clicking **"Yes"**.
6.  A progress bar will appear — wait for the download and extraction to complete. Do not interact with Kodi during this time.
7.  When prompted, click **OK** to **force close Kodi**.
8.  **Reopen Kodi** and wait for it to fully load. The first boot after the Base Pack install may take 1-2 minutes.

> 💡 **Tip:** Do NOT click anything while Kodi is initializing after this install. Let it finish on its own.

### Step 6: Install the Layout Pack

The Layout Pack applies the custom skin, menu layout, and widgets on top of the Base Pack. Install this **after** the Base Pack.

1.  After Kodi fully loads, the wizard will launch automatically again. Click **"Build Menu"**.
    *   If the prompt doesn't appear, go to **Add-ons** → **Program add-ons** → **KieranWizard**.
2.  Select **"Layout Pack"** from the list.
3.  Click **"Fresh Install"**.
4.  Confirm by clicking **"Yes"**.
5.  Wait for the download and extraction to complete.
6.  When prompted, click **OK** to **force close Kodi**.
7.  **Reopen Kodi.** The custom skin and layout should now be active.

### Step 7: Authorize Your Accounts (Setup Checklist)

After Kodi restarts with the Layout Pack installed, a **Setup Checklist** widget will appear directly on your home screen. This is designed to make authorization as easy as possible.

#### Using the Setup Checklist Widget
1.  **Authorize Real-Debrid:** Click this item. It will open the Fen Light settings. Navigate to **Accounts** -> **Real-Debrid** -> **Authorize**. Enter the code at [real-debrid.com/device](https://real-debrid.com/device).
2.  **Authorize Trakt (Fen Light):** Click this item. It will open the Fen Light settings. Navigate to **Accounts** -> **Trakt** -> **Authorize**. Enter the code at [trakt.tv/activate](https://trakt.tv/activate).
3.  **Authorize Trakt (TMDb):** Click this item. It will directly open the Trakt code window. Enter the code at [trakt.tv/activate](https://trakt.tv/activate).
4.  **Finish Setup & Restart:** Once you see green checkmarks **(✓)** next to the first three items, click this final option. Kodi will ask for confirmation and then restart. **The setup screen will then be hidden.**

---

### 🛠️ Backup Instructions (If the Widget Fails)

If clicking the widget items does not open the correct menus, or if you need to re-authorize manually at any time, follow these steps:

#### 1. Manually Authorizing Fen Light (Movies & TV)
*   Go to **Settings** (gear icon) -> **Add-ons** -> **My Add-ons** -> **Video Add-ons** -> **Fen Light** -> **Configure**.
*   **Real-Debrid:** Go to **Accounts** -> **Real-Debrid** -> **Authorize**.
*   **Trakt:** Go to **Accounts** -> **Trakt** -> **Authorize**.

#### 2. Manually Authorizing TMDb Helper (Widgets)
*   Go to **Settings** -> **Add-ons** -> **My Add-ons** -> **Video Add-ons** -> **TheMovieDb Helper** -> **Configure**.
*   **Trakt:** Go to **Accounts** -> **Trakt** -> **Authorize**.

#### 3. Re-running the Wizard Setup
*   Go to **Add-ons** -> **Program Add-ons** -> **KieranWizard**.
*   Select **Post-Install Setup** to open the original popup menu version of the checklist.
*   Select **Maintenance** -> **Clean Install** if you need to start fresh (⚠️ This wipes your data!).

---

## 🧩 Setting up Addons

If you need to manually configure addons (or if you skipped the Post-Install Setup), here's how to do it for each addon.

### 1. Fen Light (Movies & TV)
This is the main add-on for Movies and TV Shows.
*   **Location:** Settings -> Add-ons -> My Add-ons -> Video Add-ons -> **Fen Light** -> Configure.
*   **Real-Debrid:** Go to *Accounts* -> *Real-Debrid* -> Enable -> Authorize. (Follow the prompts on your device).
*   **Trakt:** Go to *Accounts* -> *Trakt* -> Authorize. (You will need to enter a code at https://trakt.tv/activate).
*   **OMDB:** Go to *Accounts* -> *Meta Accounts* -> Enable OMDB -> Enter your API Key.

### 2. Otaku Testing (Anime)
This is the main add-on for Anime.
*   **Wizard:** A setup wizard may run on first launch; follow the steps if prompted.
*   **Location:** Settings -> Add-ons -> My Add-ons -> Video Add-ons -> **Otaku Testing** -> Configure.
*   **Real-Debrid:** Go to *Accounts* -> *Debrid* -> Authorize Real-Debrid.
*   **MyAnimeList:** Go to *Accounts* -> *Tracking* -> Enable MyAnimeList -> Authorize.

### 3. TMDb Helper (Widgets/Information)
This add-on powers the home screen widgets and information screens.
*   **Location:** Settings -> Add-ons -> My Add-ons -> Video Add-ons -> **TheMovieDb Helper** -> Configure.
*   **Trakt:** Go to *Accounts* -> *Trakt* -> Authorize.
*   **OMDB:** Go to *Accounts* -> *API Keys* -> OMDB API Key -> Enter your Key.

### 4. A4k Subtitles
This provides the subtitles for your content.
*   **Location:** Settings -> Add-ons -> My Add-ons -> Subtitles -> **a4kSubtitles** -> Configure.
*   **OpenSubtitles:** Go to *Authentications* -> Enter your **OpenSubtitles.org** Username and Password.

---

## 🎮 How to Use

### Main Menu Navigation
*   **Movies/TV Shows:** Browse trending content. Use widgets to quickly jump into your next episode.
*   **Anime:** Specialized section for anime content (if using the Anime Layout).
*   **Settings:** Customize skin settings, widgets, and players.

### Keeping Your Build Updated
*   The wizard checks for layout updates automatically. If a new version is available, you'll see a notification when Kodi starts.
*   You can also check manually: **Add-ons** → **Program add-ons** → **KieranWizard** — look for `[UPDATE]` next to the build name.

### Standard Features
*   **Search:** Use the global search icon to find content across all providers.
*   **Library Integration:** Add content to your library for faster access.

---

## 🌸 Anime Configuration

If you are using the Anime features, these settings are recommended for the best experience.

### Extra Settings Needed
*   **Enable Otaku Testing Add-on:** Ensure your anime add-on (e.g., Otaku, Haru) is enabled and configured.
*   **Run the Setup Wizard:** If the setup wizard has not run, go into the top right menu -> addons -> my addons -> video addons -> otaku testing -> right click and click settings -> click run setup wizard. You need to sync Real Debrid into this add-on.
*   **Real Debrid Cloud Access:** Best way to utilize Real Debrid and watch anime. For many titles, collections come as a whole series rather than individual episodes. Search for the title you want on a media hub.

### Finding Good Collections
Criteria to look for:
*   Highlighted packs (trusted/high quality)
*   High popularity ratings
*   Multi-audio (includes dub and sub)
*   Keep an eye on file size — DO NOT exceed 100GB for most titles.
*   For current weekly releases, just watch them as they come out directly in the anime addon.

### How to Use Cloud Access
1.  Find a file collection on your cloud provider.
2.  Copy the magnet link.
3.  Go to Real-Debrid website → Cloud → Paste the link → Download
4.  Now inside the anime addon, the collection will be in your cloud. The addon will automatically grab the correct episodes with subtitles/dub.

> 💡 **Best Practice:** Use cloud torrents for completed/older anime. For currently airing/modern shows, stream them directly.

### Additional Anime Tips
*   **Watch Status Sync:** Go to the Anime Add-on Settings → *Accounts* and link your **MyAnimeList** account. This ensures your progress is saved.
*   **Debrid in Anime Add-on:** Even if you authorized Debrid for movies, you might need to re-authorize it specifically inside the Anime Add-on settings.
*   **Dub vs Sub:** Check the playback settings to prioritize your preferred audio language.
*   **Simulcasts:** Use the "Airing Now" or "Schedule" widgets to keep up with currently airing shows.
*   **Sync Issues:** If shows aren't appearing, try "Force Sync" in the add-on menu.

---

## 💡 Tips & Tricks

*   **Re-run Post-Install Setup:** If you need to re-authorize accounts, open KieranWizard from Program Add-ons and select **"Post-Install Setup"** from the main menu.
*   **Speed Up Menus:** Disable widgets you don't use in the Skin Settings to improve performance on lower-end devices.
*   **Context Menu:** Long-press (or right-click) on any item to see more options like "Trakt Manager," "Play Next," or "Related."
*   **Refresh Skin:** If a widget isn't loading, select "Reload Skin" from the Power Menu.
*   **Force Close Properly:** Always force close Kodi after installing a pack. On Windows, use Task Manager if needed. On Android/Firestick, use Force Stop from the app settings.

---

## ❓ Troubleshooting

**Issue: "No Stream Available"**
*   *Fix:* Check if your Real-Debrid subscription is active and re-authorize your account.

**Issue: Build Not Saving Settings**
*   *Fix:* Ensure you exited Kodi correctly (Force Close) after installation.

**Issue: Buffering**
*   *Fix:* Try a smaller file size link or check your internet speed.

**Issue: Skin reverts to default after install**
*   *Fix:* This means the GuiFix didn't apply correctly. Open KieranWizard → Build Menu → select your pack → click "Apply guiFix". Then force close Kodi.

**Issue: Addons showing "disabled" or grayed out**
*   *Fix:* Open KieranWizard. On startup, it should automatically enable all addons. If not, go to Maintenance → Addon Tools → Enable/Disable Addons and enable them manually.

**Issue: Wizard not appearing on startup**
*   *Fix:* Go to Add-ons → Program add-ons → KieranWizard to open it manually. The wizard runs as a startup service, but it waits for Kodi to finish loading before showing prompts.

**Issue: Post-Install Setup disappeared before I finished**
*   *Fix:* Go to Add-ons → Program add-ons → KieranWizard → **Post-Install Setup** to re-run the authorization menu.

**Issue: Real-Debrid account got banned**
*   *Fix:* You were likely sharing an account. Each person needs their own RD account. Create a new account and purchase a new subscription.

---

*Created by Kieran Amin*
