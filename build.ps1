$ErrorActionPreference = "Stop"

$projectRoot = $PSScriptRoot
$appDirectory = Join-Path $projectRoot "app"
$distDirectory = Join-Path $projectRoot "dist"
$buildDirectory = Join-Path $projectRoot "build"
$version = (Select-String -Path (Join-Path $appDirectory "constants.py") -Pattern 'VERSION = "(.+)"').Matches[0].Groups[1].Value
$bundleDirectory = Join-Path $distDirectory "GUIDownloader"
$archivePath = Join-Path $distDirectory "GUIDownloader-$version-windows-x64.zip"

python -m PyInstaller `
    --noconfirm `
    --clean `
    --windowed `
    --name GUIDownloader `
    --icon (Join-Path $projectRoot "res\images\downloading.ico") `
    --paths $appDirectory `
    --collect-data imageio_ffmpeg `
    --distpath $distDirectory `
    --workpath $buildDirectory `
    --specpath $buildDirectory `
    (Join-Path $appDirectory "main.py")

$denoExecutable = python -c "import deno; print(deno.find_deno_bin())"
Copy-Item $denoExecutable $bundleDirectory
Copy-Item (Join-Path $projectRoot "LICENSE") $bundleDirectory

Compress-Archive -Path $bundleDirectory -DestinationPath $archivePath -Force
Write-Host "Build ready: $archivePath"
