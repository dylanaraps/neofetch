## Contributors

- **[@SomaUlte](https://github.com/SomaUlte)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@dawidd6](https://github.com/dawidd6)**
- **[@mstraube](https://github.com/mstraube)**


## Operating System

- Added support for ArchBox Linux.


## General

- Fix output if subtitles are disabled and `prin` is used in an info function.


## Config

- Fixed default config not found.
- Don't set locale in config file.


## Info

**Shell**<br \>

- Fixed a crash when the user has `bash 3` installed.

**GPU**<br \>

- [Linux] Display detailed information about Intel GPUs. **[@SomaUlte](https://github.com/SomaUlte)**

**Color Blocks**<br \>

- Fixed issue with `color_blocks="off"` adding an extra newline to the output.

**Song**<br \>

- Don't print `$song` if it's empty and `song_shorthand` is on. **[@mstraube](https://github.com/mstraube)**
- Fixed `mpd` detection when `mpd` is on a different host. **[@dawidd6](https://github.com/dawidd6)**
- Use `get_song_dbus` for Audacious. **[@mstraube](https://github.com/mstraube)**


## Images

- [iTerm2] Fixed issue with linebreaks printing spaces over the image. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- Fixed issue with images not working in Terminology.
- Fixed issue when `image_source` was set to `wall`.
- [w3m-img] Fixed issues with `w3m-img` and `tmux`.


## Ascii

- [Windows 10] Fixed `ascii_distro` not working.
- Fixed a bug where the backend is `ascii` but the image_source is an image file.
