import os
import shutil

ADDON_ID = "plugin.program.kieranwizard"
ZIP_NAME = f"{ADDON_ID}.zip"
EXCLUDES = {
    ".git",
    ".gitignore",
    "__pycache__",
    "build_zip.ps1",
    "build_zip.py",
    ZIP_NAME,
    "README.MD",
    "INSTRUCTIONS.md",
    "DEPLOYMENT_CHECKLIST.MD",
    "LICENSE",
}

def create_zip():
    cwd = os.getcwd()
    zip_path = os.path.join(cwd, ZIP_NAME)
    
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"[OK] Removed old ZIP")

    print(f"=== Kodi Addon Packager ===")
    print(f"Addon   : {ADDON_ID}")
    
    # Create staging folder
    temp_dir = os.path.join(cwd, "_temp_build")
    addon_dir = os.path.join(temp_dir, ADDON_ID)
    
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(addon_dir)
    
    for item in os.listdir(cwd):
        if item in EXCLUDES or item == "_temp_build":
            continue
            
        src = os.path.join(cwd, item)
        dst = os.path.join(addon_dir, item)
        
        if os.path.isdir(src):
            # exclude __pycache__ etc inside subfolders
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        else:
            shutil.copy2(src, dst)
            
    print("Stated files in temp directory...")
    
    # Create archive
    base_name = os.path.join(cwd, ADDON_ID)
    shutil.make_archive(base_name, 'zip', temp_dir)
    
    # Clean up
    shutil.rmtree(temp_dir)
    
    print(f"\n[OK] ZIP created successfully at: {zip_path}")
    import zipfile
    print("\n--- ZIP contents (top-level) ---")
    with zipfile.ZipFile(zip_path, 'r') as z:
        for info in z.infolist()[:10]:
            print(f"  {info.filename}")
    print("--------------------------------\n")
    print("Done! Install via Kodi > Add-ons > Install from zip file.")

if __name__ == "__main__":
    create_zip()
