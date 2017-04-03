## Contributors

- **[@mstraube](https://github.com/mstraube)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@ikeydoherty](https://github.com/ikeydoherty)**
- **[@eliezio](https://github.com/eliezio)**
- **[@nilesr](https://github.com/nilesr)**
- **[@dritter](https://github.com/dritter)**


## Operating System

- Added support for SliTaz. **[@nilesr](https://github.com/nilesr)**
- Added support for Nitrux. **[@mstraube](https://github.com/mstraube)**
- Added support for DesaOS.


## Screenshot

The screenshot feature no longer requires any configuration before working. We no longer hardcode `${HOME}/Pictures/neofetch` as the screenshot location. Here's how the `-s` and `-su` flags now function:

- `neofetch -s` will save a file in the current directory named: `neofetch-$(date +%F-%I-%M-%S-${RANDOM}).png`
- `neofetch -s test.png` will save a file in the current directory called `test.png`
- `neofetch -s ~/` will save a file in `~` called `neofetch-$(date +%F-%I-%M-%S-${RANDOM}).png`
- `neofetch -s ~/test.png` will save a file in `~` called `test.png`.


## Ascii

- Arch ascii art now uses lighter colors.
- Update Parabola logo. **[@mstraube](https://github.com/mstraube)**


## Images

- Added `libsixel` backend.
- Added `termpix` backend.
- Only use a zero width space in the `w3m` backend.
- Fixed bug causing terminal size to not be found.
- [iTerm2] Fixed images not appearing inside `tmux`.


## Info

**CPU**

- Add option to show decimals in CPU speed.

**Terminal Font**

- Added \*experimental\* font detection for iTerm2. **[@dritter](https://github.com/dritter)**

**Window Manager**

- [MacOS] Added support for Kwm. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- [MacOS] Added support for Spectacle. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- [MacOS] Add support for Amethyst. **[@jorgegonzalez](https://github.com/jorgegonzalez)**

**Disk**

- Added new option to only show dir name in subtitle.

**Song**

- Fixed Audacious song output when `dbus-send` fails. **[@mstraube](https://github.com/mstraube)**

**Local IP**

- [Linux] Fixed UID showing instead of Local IP on several versions/configs of iproute2.

**Packages**

- [eopkg] Used a faster detection method. **[@ikeydoherty](https://github.com/ikeydoherty)**

**Resolution**

- [macOS] Fixed `screenresolution` not appearing at all on newer versions. **[@eliezio](https://github.com/eliezio)**
- [Linux] Show decimals.

**GPU**

- [Linux] Hide duplicate GPU lines (Only display 1).
