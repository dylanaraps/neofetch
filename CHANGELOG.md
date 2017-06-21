## Contributors

- **[@MatthewCox](https://github.com/MatthewCox)**
- **[@dawidd6](https://github.com/dawidd6)**
- **[@erikdubois](https://github.com/erikdubois)**
- **[@konimex](https://github.com/konimex)**
- **[@mstraube](https://github.com/mstraube)**
- **[@Artoriuz](https://github.com/Artoriuz)**
- **[@WilsonRU](https://github.com/WilsonRU)**
- **[@Takeya-Yuki](https://github.com/Takeya-Yuki)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@LER0ever](https://github.com/LER0ever)**


## Operating System

- Added support for IRIX.
- Added support for Arch XFerience. **[@mstraube](https://github.com/mstraube)**
- Added support for CloverOS.
- Added support for Maui. **[@mstraube](https://github.com/mstraube)**
- Added support for KS Linux. **[@Takeya-Yuki](https://github.com/Takeya-Yuki)**


## General

- Minimum required BASH version is now 3.2.
    - (Neofetch has always used 3.2+ features, I've just made it obvious now in the documentation.)
- Fixed config file not being created on first install.


## Images

- [w3m] Added `--loop` flag which makes Neofetch draw the image once per second.
    - This is a workaround to the images disappearing on resize and workspace switch.
    - Use Ctrl+C to exit.
- [w3m] Fixed w3m-img not found on FreeBSD 12. **[@Artoriuz](https://github.com/Artoriuz)**


## Ascii

- Added Ubuntu-MATE ascii art.
- Fixed ArchLabs ascii art.  **[@erikdubois](https://github.com/erikdubois)**
- Updated GoboLinux ascii art. **[@WilsonRU](https://github.com/WilsonRU)**
- Fixed `--ascii_distro windows10` not working.


## Info

**Distro**

- [Solaris, AIX, Haiku] The machine architecture will now be shown properly instead of machine ID.

**Terminal Emulator**

- Added support for Neovim terminal emulator. **[@LER0ever](https://github.com/LER0ever)**
- Added font support for mate-terminal. **[@mstraube](https://github.com/mstraube)**
- [Termite] Fix font mismatch. **[@MatthewCox](https://github.com/MatthewCox)**
- Use `$SSH_TTY` for terminal detection if machine is connected via SSH.
- Break from loop if PPID can't be accessed/not found.

**GPU**

- [Linux] Fixed GPU sort.

**Song**

- Do not detect ibus\* or indicator\* as player. **[@dawidd6](https://github.com/dawidd6)**

**Model**

- Specify when running on a Hackintosh. **[@LER0ever](https://github.com/LER0ever)**


**Memory**

- [FreeBSD]: Fix inaccurate free memory calculation.
