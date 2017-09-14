## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@mstraube](https://github.com/mstraube)**
- **[@dominiklohmann](https://github.com/dominiklohmann)**
- **[@ybden](https://github.com/ybden)**
- **[@lexruee](https://github.com/lexruee)**
- **[@AMDmi3](https://github.com/AMDmi3)**
- **[@deadda7a](https://github.com/deadda7a)**
- **[@winneon](https://github.com/winneon)**
- **[@DamnWidget](https://github.com/DamnWidget)**


## General

- Config file now has a `.conf` suffix.
- Neofetch now assumes target directories (config file and ASCII directory) at install time, this fixes problems with systems such as NixOS.
- `stdout` mode is now reimplemented.
    - This mode prints the information in plain text.
    - You can use it with `--stdout`.
    - Example: https://gist.github.com/dylanaraps/151c205322cf3acae62661b76464a3f7
- Fixed prompt location if color blocks are disabled.
- Make makefile more portable. **[@AMDmi3](https://github.com/AMDmi3)**


## Operating System

- Added support for AryaLinux. **[@mstraube](https://github.com/mstraube)**
- Added support for Amazon Linux AMI.
- Added support for Artix Linux. **[@DamnWidget](https://github.com/DamnWidget)**
- Added support for Endless OS.
- Added support for Sabotage Linux.
- Added support for Siduction. **[@lexruee](https://github.com/lexruee)**
- Added support for Source Mage.
- Added support for Parsix GNU/Linux. **[@mstraube](https://github.com/mstraube)**
- Added support for Nurunner. **[@mstraube](https://github.com/mstraube)**
- Fixed Raspbian being detected as ChromeOS.


## Images

- [w3m] Fixed w3m-img not found on NixOS.
- Added support for using all image types as input.
    - Neofetch now supports `svg`, `tiff` etc.


## ASCII

- Added small Debian.
- Added small FreeBSD.
- Added small macOS.
- Added small NixOS.


## Info

**GPU Driver**

- [Linux] Added a new info function (*off by default*) to display the GPU Driver currently in use.
- Add `info "GPU Driver" gpu_driver` to your config to use it.

**CPU**

- [Linux] Fixed inaccurate output on ARM SoC devices.
- [Linux] Fixed CPU speed not appearing on PowerPC systems.
- [NetBSD] Added support for CPU temperature. (NOTE: This only supports newer Intel processors)
- Fixed inaccurate speed output in systems with CPU speed less than 1 GHz.
- Deprecated `cpu_shorthand` in favor of `cpu_brand`.

**GPU**

- [Linux] Filter out duplicate entries.

**Model**

- Added support for QEMU/KVM.
- Renamed subtitle to `Host:`.

**Uptime**

- [AIX/IRIX] Fixed Neofetch crashing when calculating uptime.

**Terminal**

- [SSH] Fixed infinite loop if neofetch is run on non-interactive shells.

**Terminal Font**

- Added support for LXTerminal. **[@mstraube](https://github.com/mstraube)**
- Added support for GNUStep Terminal. **[@mstraube](https://github.com/mstraube)**
- Fixed Xfce4-terminal font output when system-wide font is used. **[@mstraube](https://github.com/mstraube)**
- Fixed MATE-Terminal issue. **[@mstraube](https://github.com/mstraube)**
- Fixed URxvt font detection failing if `.` is used. **[@winneon](https://github.com/winneon)**

**Theme**

- [Qt/KDE] Fixed inaccurate theme naming. **[@mstraube](https://github.com/mstraube)**
- [Qt/KDE] GTK theme is now shows as well.

**Window Manager**

- [macOS] Added support for `chunkwm`. **[@dominiklohmann](https://github.com/dominiklohmann)**
- Fix incorrect output when using WindowMaker. **[@mstraube](https://github.com/mstraube)**

**Song**

- Added support for Pogo. **[@mstraube](https://github.com/mstraube)**
- Fixed bug with players not being found.

**Battery**

- Added battery support for Thinkpads and other devices that use the `CMB` naming for batteries. **[@deadda7a](https://github.com/deadda7a)**


## Images

- Fixed division by 0 error in XTerm.

## Screenshot

- Use `maim` over `scrot`. **[@ybden](https://github.com/ybden)**
- Fixed `scrot_cmd` arguments not being used. **[@winneon](https://github.com/winneon)**
