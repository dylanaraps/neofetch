# Neofetch

[![Gitter](https://badges.gitter.im/dylanaraps/fetch.svg)](https://gitter.im/dylanaraps/fetch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Build Status](https://travis-ci.org/dylanaraps/neofetch.svg?branch=master)](https://travis-ci.org/dylanaraps/neofetch) [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) [![Latest release](https://img.shields.io/github/release/dylanaraps/neofetch.svg)](https://github.com/dylanaraps/neofetch/releases)

Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ascii file of your choice. The main purpose of neofetch is to be used in screenshots to show other users what OS/Distro you're running, what Theme/Icons you're using and etc.

Neofetch is highly customizable through the use of commandline flags or the user config file. There are over 50 config options to mess around with and there's the `print_info()` function and friends which let you add your own custom info.

Neofetch can be used on any OS that has BASH, it's just a matter of adding support. If your OS/Distro isn't in the list below, feel free to open an issue on the repo and I'll gladly add support. Neofetch currently supports `Linux`, `MacOS`, `iOS`, `BSD`, `Solaris`, `Android`, `Haiku`, `GNU Hurd` and `Windows (Cygwin/Windows 10 Linux subsystem)`.

For more information:

**https://github.com/dylanaraps/neofetch/wiki**

![1](https://ipfs.pics/ipfs/QmTtF9Sx8o617QE88GH3Z4yX7mRyi4yS1hsMHyRVmn14vJ)


## Dependencies

https://github.com/dylanaraps/neofetch/wiki/Dependencies


## Installation

https://github.com/dylanaraps/neofetch/wiki/Installation


## Post Install


### Using the config file

Neofetch will by default create a config file at `$HOME/.config/neofetch/config` and this file contains all of the script's options/settings. The config file allows you to keep your customizations between script versions and allows you to easily share your customizations with other people.

You can launch the script without a config file by using the flag `--config none` and you can specify a custom config location using `--config path/to/config`.

See this wiki page for the default config: https://github.com/dylanaraps/neofetch/wiki/Config-File


### Customizing what info gets displayed

https://github.com/dylanaraps/neofetch/wiki/Customizing-Info


### Customizing the script using a custom alias

If you don't want to use the config file you can customize almost everything using launch flags!

Here's an example neofetch alias:

```sh
alias neofetch2="neofetch \
--config off \
--block_range 1 8 \
--bold off \
--uptime_shorthand on \
--gtk_shorthand on \
--colors 4 1 8 8 8 7 \
"
```


## Thanks

Thanks to:

- [Contributors](https://github.com/dylanaraps/neofetch/contributors)
    - Thanks for making Neofetch better, I really appreciate it.
- [Packagers](https://github.com/dylanaraps/neofetch/issues/115)
    - Thanks for maintaining Neofetch packages.
- Users
    - Thanks for using my script!
- [Screenfetch](https://github.com/KittyKatt/screenFetch):
    - I've used some snippets as a base for a few functions in this script.
    - Some of the ascii logos.
- [ufetch](https://github.com/jschx/ufetch):
    - Tiny ascii logos
