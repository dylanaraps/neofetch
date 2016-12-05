## Contributors

- **[@konimex](https://github.com/konimex)**


## Info

**Distro**<br \>

- Added support for Apricity OS.
- Added support for GoboLinux. **[@konimex](https://github.com/konimex)**
- Added support for SwagArch.
- Added support for AOSC OS.
- Fixed bug that caused Linux Mint systems to be identified as Ubuntu.
- Fixed bug that caused CentOS systems to not be detected.

**Memory**<br \>

- [BSD] Fixed high memory output.

**GPU**<br \>

- [Linux] Fixed bug where sound card was detected as GPU.

**Packages**<br \>

- Only call `wc -l` once at the end of the function instead of calling it once per package manager.

**Desktop Environment**<br \>

- Show Cinnamon version.


## Image

- Changed default image mode to `ascii`.
    - See: [Images in the terminal](https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal#enabling-image-mode)


## Wallpaper

- Rewrote wallpaper function.
- Prioritize DE wallpaper setters before falling back to `feh`/`nitrogen`.
- Added support for XFCE's wallpaper setter.


## Ascii

![ubuntu](https://u.teknik.io/zILeY.png)
<br \><sub>Old Ubuntu Logo vs New Ubuntu Logo</sub>

- Updated Ubuntu logo to the latest version.
    - You can use the old logo by launching neofetch with `--ascii_distro ubuntu_old` or by changing `$ascii_distro` to `ubuntu_old` in your config file.
- `--ascii_colors` no longer changes text colors.
- Fixed bug causing RFRemix to use the incorrect ascii art.
