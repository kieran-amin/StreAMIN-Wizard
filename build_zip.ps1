# ============================================================
#  build_zip.ps1  –  Package plugin.program.kieranwizard
#  Run from the project root:  .\build_zip.ps1
# ============================================================

$AddonId   = "plugin.program.kieranwizard"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$OutDir    = $ScriptDir          # ZIP lands in the project root
$ZipName   = "$AddonId.zip"
$ZipPath   = Join-Path $OutDir $ZipName

# Files/folders to EXCLUDE from the package
$Exclude = @(
    ".git",
    ".gitignore",
    "__pycache__",
    "build_zip.ps1",
    "build_zip.py",
    "BETA_TEST_PLAN.md",
    "DEPLOYMENT_CHECKLIST.MD",
    $ZipName,
    "README.MD",
    "INSTRUCTIONS.md",
    "LICENSE"
)

Write-Host "`n=== Kodi Addon Packager ===" -ForegroundColor Cyan
Write-Host "Addon   : $AddonId"
Write-Host "Output  : $ZipPath`n"

# Remove old ZIP if it exists
if (Test-Path $ZipPath) {
    Remove-Item $ZipPath -Force
    Write-Host "[✓] Removed old ZIP" -ForegroundColor Yellow
}

# Create a temp staging directory with the required top-level folder
$TempRoot   = Join-Path $env:TEMP "kodi_addon_build"
$TempAddon  = Join-Path $TempRoot $AddonId

if (Test-Path $TempRoot) { Remove-Item $TempRoot -Recurse -Force }
New-Item -ItemType Directory -Path $TempAddon | Out-Null
Write-Host "[✓] Created staging folder: $TempAddon" -ForegroundColor DarkGray

# Copy addon files into the staging folder
Get-ChildItem -Path $ScriptDir | Where-Object {
    $Exclude -notcontains $_.Name
} | ForEach-Object {
    $Dest = Join-Path $TempAddon $_.Name
    if ($_.PSIsContainer) {
        Copy-Item -Path $_.FullName -Destination $Dest -Recurse -Force
    } else {
        Copy-Item -Path $_.FullName -Destination $Dest -Force
    }
    Write-Host "  + $($_.Name)"
}

# Compress from the TEMP ROOT so the ZIP contains: plugin.program.kieranwizard/
Compress-Archive -Path $TempAddon -DestinationPath $ZipPath -CompressionLevel Optimal
Write-Host "`n[✓] ZIP created: $ZipPath" -ForegroundColor Green

# Cleanup
Remove-Item $TempRoot -Recurse -Force
Write-Host "[✓] Temp files cleaned up`n"

# Verify structure
Write-Host "--- ZIP contents (top-level) ---" -ForegroundColor Cyan
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($ZipPath)
$zip.Entries | Select-Object -First 20 | ForEach-Object { Write-Host "  $($_.FullName)" }
$zip.Dispose()
Write-Host "--------------------------------`n"
Write-Host "Done! Install via Kodi > Add-ons > Install from zip file." -ForegroundColor Green
