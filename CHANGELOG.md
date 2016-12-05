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
- Added support for Solaris and GNU Hurd. **[@konimex](https://github.com/konimex)**


## Ascii

![ubuntu](https://u.teknik.io/zILeY.png)
<br \><sub>Old Ubuntu Logo vs New Ubuntu Logo</sub>

- Updated Ubuntu logo to the latest version.
    - You can use the old logo by launching neofetch with `--ascii_distro ubuntu_old` or by changing `$ascii_distro` to `ubuntu_old` in your config file.
- `--ascii_colors` no longer changes text colors.
- Fixed bug causing RFRemix to use the incorrect ascii art.


## Screenshots

Neofetch will now automatically find and use whatever screenshot tool is available on your system. The screenshot tool is no longer hardcoded and you don't have to edit your config file to specify what program to use.

On Haiku and macOS, Neofetch will use the built-in tools to take screenshots. On systems with an X server Neofetch will look for and use the following programs: `scrot`, `maim`, `import (imagemagick)`, `imlib2_grab` and `gnome-screenshot`. 

The config option `scrot_cmd` and the commandline flag `--scrot_cmd` are still there for those who want to use custom flags, programs or scripts to take screenshots. 

- Automatically use whatever screenshot tool is available.
- Added screenshot support to macOS
- Added screenshot support to Haiku


## Screenshot Upload

- [teknik.io] Fixed images not uploading with the right filetype.
- Changed default image upload host to `teknik.io`.
    - teknik doesn't compress images whereas imgur does.
    - You can change this back to imgur by using `--image_host imgur` or by editing your config file.
