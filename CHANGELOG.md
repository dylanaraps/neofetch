## Contributors

**[@mstraube](https://github.com/mstraube)**


## General

- Config file now has a `.conf` suffix.
- Neofetch now assumes target directories (config file and ASCII directory) at install time, this fixes problems with systems such as NixOS.


## Operating System

- Added support for Sabotage Linux.


## Info

**CPU**

- [Linux] Fixed inaccurate output on ARM SoC devices.
- [Linux] Fixed CPU speed not appearing on PowerPC systems.
- [NetBSD] Added support for CPU temperature. (NOTE: This only supports newer Intel processors)
- Fixed inaccurate speed output in systems with CPU speed less than 1 GHz.

**Terminal**

- [SSH] Fixed infinite loop if neofetch is run on non-interactive shells.

**Theme**

- [Qt/KDE] Fixed inaccurate theme naming. **[@mstraube](https://github.com/mstraube)**

## Images

- Fixed division by 0 error in XTerm.
