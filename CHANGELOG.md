## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@mstraube](https://github.com/mstraube)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@ikeydoherty](https://github.com/ikeydoherty)**
- **[@eliezio](https://github.com/eliezio)**
- **[@nilesr](https://github.com/nilesr)**
- **[@dritter](https://github.com/dritter)**
- **[@HebaruSan](https://github.com/HebaruSan)**
- **[@LER0ever](https://github.com/LER0ever)**
- **[@obrevenge](https://github.com/obrevenge)**
- **[@ajjames31](https://github.com/ajjames31)**
- Eliezio Oliveira


## Operating System

- Added Chrome OS Crouton support. **[@LER0ever](https://github.com/LER0ever)**
- Added support for SliTaz. **[@nilesr](https://github.com/nilesr)**
- Added support for Nitrux. **[@mstraube](https://github.com/mstraube)**
- Added support for DesaOS.
- Added support for MinGW.
- Added support for OBRevenge. **[@obrevenge](https://github.com/obrevenge)**
- Added support for ArchLabs. **[@obrevenge](https://github.com/obrevenge)**


## Screenshot

The screenshot feature no longer requires any configuration before working. We no longer hardcode `${HOME}/Pictures/neofetch` as the screenshot location. Here's how the `-s` and `-su` flags now function:

- `neofetch -s` will save a file in the current directory named: `neofetch-$(date +%F-%I-%M-%S-${RANDOM}).png`
- `neofetch -s test.png` will save a file in the current directory called `test.png`
- `neofetch -s ~/` will save a file in `~` called `neofetch-$(date +%F-%I-%M-%S-${RANDOM}).png`
- `neofetch -s ~/test.png` will save a file in `~` called `test.png`.


## ASCII

- Arch ASCII art now uses lighter colors.
- Fixed Ubuntu-Studio ASCII setting. **[@@HebaruSan](https://github.com/HebaruSan)**
- Updated Parabola logo. **[@mstraube](https://github.com/mstraube)**
- Updated Raspbian ASCII art.


## Images

- Added `libsixel` backend.
- Added `termpix` backend.
- Only use a zero width space in the `w3m` backend.
- Fixed bug causing terminal size to not be found.
- [iTerm2] Fixed images not appearing inside `tmux`.


## Info

**Locale**

- Added a new function to display system locale. (Disabled by default)

**CPU**

- Added option to show decimals in CPU speed.

**Terminal Font**

- Added \*experimental\* font detection for iTerm2. **[@dritter](https://github.com/dritter)**

**Window Manager**

- [MacOS] Added support for Kwm. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- [MacOS] Added support for Spectacle. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- [MacOS] Added support for Amethyst. **[@jorgegonzalez](https://github.com/jorgegonzalez)**

**Battery**

- Added battery support for Bay Trail devices.  **[@mstraube](https://github.com/mstraube)**

**Disk**

- Added new option to only show dir name in subtitle.

**Song**

- Added support for Deepin Music. **[@mstraube](https://github.com/mstraube)**
- Added support for Tomahawk. **[@mstraube](https://github.com/mstraube)**
- Fixed Audacious song output when `dbus-send` fails. **[@mstraube](https://github.com/mstraube)**

**Local IP**

- [Linux] Fixed UID showing instead of Local IP on several versions/configs of iproute2.

**Packages**

- [eopkg] Use a faster detection method. **[@ikeydoherty](https://github.com/ikeydoherty)**

**Resolution**

- [macOS] Fixed `screenresolution` not appearing at all on newer versions. **[@eliezio](https://github.com/eliezio)**
- [Linux] Show decimals.

**GPU**

- [Linux] Hide duplicate GPU lines (Only display 1).
