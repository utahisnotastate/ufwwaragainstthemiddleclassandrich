# Kernel Payload

Place the compiled Lazarus Kernel here:

```
m5_integrated_kernel.bin
```

## Build locally

```powershell
cd M5-Utah
.\scripts\build_kernel.ps1 -Board cores3
```

The script copies `firmware.bin` from PlatformIO output into this folder.

## Distribution

Ship this `.bin` alongside `run_omni_flash.py` (or a packaged `omni_flash.exe`). The binary is not committed to git — build per board target (`cores3`, `core2`, `atoms3`).
