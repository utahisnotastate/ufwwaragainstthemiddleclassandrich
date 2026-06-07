# Build M5IntegratedKernel and copy firmware.bin to payloads/
param(
    [ValidateSet("cores3", "core2", "atoms3")]
    [string]$Board = "cores3"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$FirmwareDir = Join-Path $Root "firmware\M5IntegratedKernel"
$PayloadDir = Join-Path $Root "payloads"

Push-Location $FirmwareDir
try {
    pio run -e $Board
    $BuildDir = Join-Path $FirmwareDir ".pio\build\$Board"
    $Src = Join-Path $BuildDir "firmware.bin"
    if (-not (Test-Path $Src)) {
        throw "Build succeeded but firmware.bin not found at $Src"
    }
    Copy-Item $Src (Join-Path $PayloadDir "m5_integrated_kernel.bin") -Force
    Write-Host "[OK] Kernel copied to payloads/m5_integrated_kernel.bin ($Board build)"
}
finally {
    Pop-Location
}
