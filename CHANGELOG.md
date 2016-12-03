## Neofetch 2.0.1

## Contributors

- **[@konimex](https://github.com/konimex)**


## Info

**Distro**<br \>

- Added support for Apricity OS.
- Added support for GoboLinux. **[@konimex](https://github.com/konimex)**
- Added support for SwagArch.
- Fixed bug that caused Linux Mint systems to be identified as Ubuntu.

**Packages**<br \>

- Optimized `get_packages()` function to only call `wc -l` once at the end of the function instead of once per package manager.


## Image

- Changed default image mode to `ascii`.
    - See: [Images in the terminal](https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal#enabling-image-mode)


## Ascii

![ubuntu](https://u.teknik.io/zILeY.png)
<br \><sub>Old Ubuntu Logo vs New Ubuntu Logo</sub>

- Updated Ubuntu logo to the latest version.
- `--ascii_colors` no longer changes text colors.
