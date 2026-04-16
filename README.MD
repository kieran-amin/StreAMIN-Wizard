Welcome to the official tutorial for KieranWizard! This guide will walk you through everything you need to know—from installation to advanced tips and tricks.

## ⚠️ READ THIS FIRST — Common Questions & Rules

> **Stop.** Read this entire section before texting/calling me. If you call me and I can tell it's your first time reading these instructions, I will come find you. Charles, don't make me come to Madison. 

1. **Why do I need Real-Debrid?**
   Real-Debrid is a multi-hoster caching service. It caches data on its high-speed servers and provides direct access — meaning you access content from their secure servers rather than via public peer networks. It also acts as an encrypted layer so your connection is protected. TLDR: You can stream content without getting caught. 

2. **Each person MUST have their own Real-Debrid account.**
   > ⚠️ **DO NOT share a Real-Debrid account with anyone, even within the same household or city.** Real-Debrid actively monitors for account sharing. If two people use the same account from different IPs (even in the same city), your account **WILL be permanently banned** with no refund. I learned this the hard way. Buy your own subscription — it's like $4/month. This is non-negotiable. You will setup this via an app called Privacy on your phone. Download that now. 

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
  - [Step 5: Install the Build](#step-5-install-the-build)
  - [Step 6: Authorize Your Accounts](#step-6-authorize-your-accounts-setup-checklist)
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
2.  **Choosing the Right Version:**
    *   **🍎 macOS:** If you have a modern Mac (M1, M2, M3), you **MUST** download the **Apple Silicon ARM64** version. 
        *   *To verify:* Click the **Apple menu ** (top-left) -> **About This Mac**. Look for **"Chip"**. If it says Apple M1/M2/M3, you need **ARM64**.
    *   **🖥️ Windows:** Most PCs require the **Installer (64BIT)** version. 
        *   *To verify:* Go to **Settings** -> **System** -> **About**. Look for **"System type"** to confirm it says **64-bit**.
3.  Run the installer and follow the on-screen prompts.
4.  Launch Kodi once and let it finish its initial setup.

### Step 2: Enable Unknown Sources
I recommend using arrow keys and enter key to navigate Kodi (especially the setup). Once you have my build installed, mouse works a little better. I still use arrow keys. 
Kodi blocks third-party add-on installations by default. You must enable "Unknown Sources" to install the wizard.

1.  From the Kodi home screen, click the **gear icon** ⚙️ (top-left) to open **Settings**.
2.  Click **System**.
3.  On the left sidebar, click **Add-ons**.
4.  > ⚠️ **Important:** If you don't see the "Add-ons" option in System settings, you may need to change the settings level. In the bottom-left corner of the Settings page, click the gear icon until it says **"Advanced"** or **"Expert"**.
5.  Toggle **"Unknown sources"** to **ON**.
6.  A warning popup will appear — click **Yes** to confirm.
7.  Press **Esc** or **Back** to return to the home screen.


### Step 3: Download the Wizard

1.  Go to the KieranWizard GitHub **Releases** page: [https://github.com/kieran-amin/StreAMIN-Wizard/releases](https://github.com/kieran-amin/StreAMIN-Wizard/releases)
2.  Click the **latest release** at the top.
3.  Under **"Assets"**, click **`plugin.program.kieranwizard-1.0.0.zip`** to download it.
4.  **Do not unzip it.** Kodi installs directly from the `.zip` file.
5.  Note where the file saved — by default it goes to your **Downloads** folder.

---

### Step 4: Install the Wizard from Zip File

1.  From the Kodi home screen, click **Add-ons** in the left sidebar.
2.  Click the **open box icon** 📦 in the top-left corner — this opens the Add-on browser.
3.  Select **"Install from zip file"**.
4.  If a popup about Unknown Sources appears, click **Settings** and enable it (see Step 2), then come back.
5.  A file browser will open. The easiest way to find your file is to select **`Home folder`**:

- Scroll up and click **`Home folder`**.
- Open the **`Downloads`** folder.
- Find and click **`plugin.program.kieranwizard-1.0.0.zip`**.

> ⚠️ **Can't find "Home folder"?** Keep scrolling up past `Root filesystem` until you see it, or look under:
> - **Windows:** `C:` → `Users` → `(your username)` → `Downloads`
> - **macOS:** `Users` → `(your username)` → `Downloads`

6.  Wait for the **"KieranWizard Add-on installed"** notification to appear in the top-right corner. This may take 10-20 seconds.

> ⚠️ **IMPORTANT:** Ensure you **do not have a VPN active** during the installation process as it can interfere with the downloads.

### Step 5: Install the Build

1.  After the wizard is installed, **restart Kodi** — close it completely and reopen it.
2.  A popup will appear automatically saying **"Build Menu"** — click it to open the build menu.
    *   If it doesn't appear, go to **Add-ons** → **Program add-ons** → **KieranWizard** manually.
3.  A first-time settings screen appears. **Do not change any settings** — just click **Continue**.
4.  You are now in the **Build Menu** — a tile-based screen with options including **Current Build**, **Build Information**, and **Save Data Menu**.
5.  Click the teal **`(KieranWizard) Install`** tile.
6.  A progress bar will appear — wait for the download and extraction to complete.
    *   💡 **Note:** If you see any errors during this part, **ignore them** — it should be fine.
7.  When prompted, click **OK** to **force close Kodi**.
8.  **Reopen Kodi** and wait for it to fully load. Your build is installed.

### Step 6: Authorize Your Accounts (Setup Checklist)

After reopening Kodi, you will see a setup checklist on the home screen. Work through each step in order.

> ⚠️ **For each step, an instruction dialog will appear first** — read it carefully, then click **OK** to open the addon settings. When you're done in settings, close them and answer **"Yes"** when asked if you authorized successfully.

1.  **Step 1 — TMDb Helper:**
    *   Click the Step 1 item → read the instructions → click **OK**.
    *   TMDb Helper settings open. Go to **Accounts** → **Trakt** → **Authorize**.
    *   Also go to **API Keys** → enter your **OMDb API Key**.
    *   Close settings → click **Yes** when asked if you authorized.

2.  **Step 2 — Subtitles (Optional):**
    *   Click the Step 2 item → read the instructions → click **OK**.
    *   a4kSubtitles settings open. Go to **Authentications** → enter your **OpenSubtitles** username and password.
    *   Close settings → click **Yes** when done (or skip if you don't use subtitles).

3.  **Step 3 — Fen Light:**
    *   Click the Step 3 item → read the instructions carefully → click **OK**.
    *   Fen Light settings will open. **If an internal setup wizard appears, press Backspace to dismiss it first.**
    *   Then go to **Sources Accounts** → **Real Debrid** → **Authorize**.
    *   Enter the code displayed at [real-debrid.com/device](https://real-debrid.com/device).
    *   Also go to **Meta Accounts** → **Trakt** → **Authorize**.
    *   Enter the code displayed at [trakt.tv/activate](https://trakt.tv/activate).
    *   Close settings → click **Yes** when asked if you authorized.

4.  **Finish Setup:**
    *   Click **">> Finish Setup <<"** to hide the checklist and return to your home screen.

**Your build is now fully set up and ready to use!**

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

*   **Force Close Properly:** Always force close Kodi after installing a pack. On Windows, use Task Manager if needed. On Android/Firestick, use Force Stop from the app settings.

### ⌨️ Handy Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| **C** / **Right Click** | Open Context Menu (Subtitles, Trakt Manager, etc.) |
| **I** | Show Information (Ratings, Plot, Cast) |
| **Backspace** | Go Back (Return to previous screen) |
| **Esc** | Go Home (Return to main home screen) |
| **Space** / **P** | Play / Pause |
| **X** | Stop Playback |
| **F** | Toggle Fullscreen |
| **M** | Show Player Controls |
| **S** | Open Power / Restart Menu |
| **Page Up / Down** | Skip 10 minutes Forward / Backward |
| **Arrows** | Small step seek (Forward/Backward) |

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
