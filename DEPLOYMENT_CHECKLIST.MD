# 🚀 KieranWizard Deployment Checklist

Before you share the wizard with other users, ensure you have completed these final steps.

## 1. Documentation & Files
- [x] **README.md (GitHub)**: Simplified version created.
- [x] **INSTRUCTIONS.md (Internal)**: Detailed setup checklist and backup instructions added.
- [ ] **ZIP the Addon**: Compress the `plugin.program.kieranwizard` folder into a ZIP file.
    - Name it `plugin.program.kieranwizard-1.0.0.zip` (match the version in `addon.xml`).
    - **Crucial**: Ensure no personal files (like `settings.xml` with your passwords or `textures.db` with your history) are inside the ZIP if you are including them from your own Kodi install.

## 2. Hosting & Connectivity
- [ ] **Host `builds.txt`**: Upload this file to a static URL (e.g., GitHub Gist, GitHub Pages, or a raw file in your repo).
- [ ] **Update `uservar.py`**:
    - Change line 20: `BUILDFILE = 'https://raw.githubusercontent.com/username/repo/main/builds.txt'`
- [ ] **Host your Packs**: 
    - Upload the Base Pack and Layout Pack ZIPs to a server or GitHub.
    - Update the `url="..."` links inside your hosted `builds.txt` to point to these live URLs.

## 3. Remote Updating Mechanism
To allow users to receive layout updates automatically:
1.  **Modify your local layout**: Make changes to the skin/menus in your own Kodi.
2.  **Export the new Layout Pack**: Create a new ZIP from your modified files.
3.  **Upload & Version**:
    - Upload the new ZIP to your server.
    - Update the version number in your hosted `builds.txt` (e.g., from `3.2` to `3.3`).
    - The wizard checks `BUILDFILE` every startup (as `UPDATECHECK = 0` in `uservar.py`) and will notify users of the update.

## 4. Authorization & Passcodes
- [ ] **Verify Master Passcode**: Current hardcoded master is `KIERAN2026` in `wizard.py`.
- [ ] **Setup Auth DB (Optional)**:
    - If you want to use unique passcodes for different people, host a JSON file at the URL on line 60 of `wizard.py`.
    - Format:
      ```json
      {
        "passcodes": {
          "USER_CODE_1": {"status": "active", "note": "Kieran's Friend"},
          "USER_CODE_2": {"status": "expired", "note": "Old Test"}
        }
      }
      ```

## 5. Security Check
- [ ] **Remove Credentials**: Search the entire project for any hardcoded API keys or passwords you don't want to share.
- [ ] **Check `builds.txt`**: Ensure the `url` fields are not pointing to `localhost`.

---

### Installing on Another Laptop
1.  Send them the `plugin.program.kieranwizard-1.0.0.zip`.
2.  Tell them to follow the **Installation** section in the `README.md`.
3.  Provide them with the passcode (`KIERAN2026` or a custom one) when they install the **Layout Pack**.
4.  Once they install the layout, guide them to the **Setup Checklist** on their home screen.
