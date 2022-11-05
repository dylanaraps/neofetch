# HyFetch

neofetch with pride flags <3

<img alt="screenshot" src="https://user-images.githubusercontent.com/22280294/197708447-ddee6db2-1017-48f2-b507-8ddf85acef0d.png">

### Running Updated Original Neofetch

This repo also serves as an updated version of the original `neofetch` since the upstream [dylanaraps/neofetch](https://github.com/dylanaraps/neofetch) doesn't seem to be maintained anymore (as of Jul 30, 2022, the original repo hasn't merged a pull request for 6 months). If you only want to use the updated neofetch without pride flags, you can use the `neofetch` script from this repo. To prevent command name conflict, I call it `neowofetch` :)

* Method 1: `pip install hyfetch` then run `neowofetch`
* Method 2: `npx neowofetch`
* Method 3: `bash <(curl -sL neowofetch.hydev.org)`


## Installation

### Method 1: Install using Python pip (Recommended)

Install Python >= 3.7 first. Then, just do:

```sh
pip install hyfetch
```

### Method 2: Install using system package manager

Currently, these distributions have existing packages for HyFetch:

* Arch Linux: `paru -S hyfetch` or `yay -S hyfetch` (Thanks to [@Aleksana](https://github.com/Aleksanaa))
* Nix: `nix-env -i hyfetch` (Thanks to [@YisuiDenghua](https://github.com/YisuiDenghua))
* Guix: `guix install hyfetch` (Thanks to [@WammKD](https://github.com/WammKD))

### Method 3: Install the latest developmental version using git

Install Python >= 3.7 first. Then run the following commands:

```sh
git clone https://github.com/hykilpikonna/hyfetch.git
cd hyfetch
pip install .
```


## Usage

When you run `hyfetch` for the first time, it will prompt you to choose a color system and a preset. Just follow the prompt, and everything should work (hopefully). If something doesn't work, feel free to submit an issue!

If you want to use the updated `neofetch` without LGBTQ flags, check out [this section](https://github.com/hykilpikonna/hyfetch#running-updated-original-neofetch)


## Questions and answers

#### Q: How do I change my config?

A: Use `hyfetch -c`

#### Q: What do I do if the color is too dark/light for my theme?

A: You can try setting the colors' "lightness" in the configuration menu. The value should be between 0 and 1. For example, if you are using dark theme and the rainbow flag is too dark to display, you can set lightness to 0.7.

Feel free to experiment with it!

![image](https://user-images.githubusercontent.com/22280294/162614553-eb758e4e-1936-472c-8ca7-b601c696c6eb.png)


## Contributing

To make changes to our codebase, you first need to create a fork by clicking the "Fork" button on the top right. Then, you can clone your fork of the source code using `git clone https://github.com/{your username}/hyfetch.git`.

After making changes to the source code, you can run `python -m hyfetch` in the root directory of your repo to test out your changes.

If they work correctly, you can commit and push these changes using git command or Github Desktop. Then, you can create a pull request on Github so that it can go into our next release!

You can also install your version locally by running `pip install .` in the repo root.


## Change Log

### About Notation

Updates to HyFetch begins with the emoji 🌈  
Updates to `neowofetch` begins with the emoji 🖼️

### TODO

* [ ] (Important!) Refactor flag storage & coloring to support non-stride patterns
* [ ] Config menu: Allow left-right arrow keys for pagination

<!-- CHANGELOG STARTS HERE --->

### Unpublished 1.4.4

Note: You can install the latest nightly version by using:

```sh
pip install git+https://github.com/hykilpikonna/hyfetch.git@master
```

* 🌈 Fix Python 3.11 compatibility (#35)
* 🖼️ Memory - Optimize and fix memory unit conversion (dylanaraps/neofetch#2225)
* 🖼️ CPU - Fix model detection for loongson (#34)

### 1.4.3

* 🌈 **Auto detect terminal background color & rgb support**
* 🌈 **Optimize experience on light-themed terminals**
* 🌈 Fix bugs with lightness and light-mode config not applying
* 🌈 Fix color alignment for distros with first color ≠ `${c1}` (e.g. Ubuntu Budgie)
* 🌈 Add unlabeled flags (#25)
* 🌈 Add gender nonconforming & femboy & tomboy flags (#32)
* 🌈 Fix jailbreak iOS shell `killed: 9` issue caused by ld signature check.
* 🖼️ Distro - Add garuda_small ([dylanaraps#2215](https://github.com/dylanaraps/neofetch/pull/2215))
* 🖼️ Distro - Add Cobalt Linux ([dylanaraps#2213](https://github.com/dylanaraps/neofetch/pull/2213))
* 🖼️ Distro - Add VanillaOS ([dylanaraps#2222](https://github.com/dylanaraps/neofetch/pull/2222))
* 🖼️ Distro - Surround macOS build number in parentheses (#28)
* 🖼️ Misc - Auto select stdout mode based on tty detection (#31)
* 🖼️ Bug Fix - Fix cols coloring reset for bash 3.2 (#24)

### 1.4.2

* 🌈 Detailed runnning/contributing instructions in README.md (#21)
* 🖼️ Distro - Add Stock Linux (#23)
* 🖼️ Distro - Add DietPi ([dylanaraps#1706](https://github.com/dylanaraps/neofetch/pull/1706))
* 🖼️ Distro - Add OmniOS illumos ([dylanaraps#2196](https://github.com/dylanaraps/neofetch/pull/2196))
* 🖼️ Distro - Add Droidian ([dylanaraps#2201](https://github.com/dylanaraps/neofetch/pull/2201))
* 🖼️ Distro - Add HamoniKR ([dylanaraps#2210](https://github.com/dylanaraps/neofetch/pull/2210))
* 🖼️ Song - Add support for TIDAL HiFi (#22)
* 🖼️ CPU - Detect multiple CPU models for ARM
* 🖼️ Misc - Better defaults: Show RAM in GiB, RAM percentage, CPU speed rounding, refresh rate
* 🖼️ Bug Fix - Fix bash 5.2 column cut off issue (#24)

### 1.4.1

* 🌈 Paginate flags (#14)
* 🌈 Add release workflow (#15)
* 🌈 Create automatic release script
* 🌈 Config page - Give warning when terminal size is too small
* 🌈 Config page - Optimize color arrangement selection on small screens
* 🌈 Add experimental Windows support (very unstable at the moment)
* 🖼️ Distro - Add ravynOS ([dylanaraps#2182](https://github.com/dylanaraps/neofetch/pull/2182))
* 🖼️ Distro - Add ChonkySealOS ([dylanaraps#2180](https://github.com/dylanaraps/neofetch/pull/2180))
* 🖼️ Distro - Add GhostBSD ([TheSudoer#18](https://github.com/hykilpikonna/hyfetch/pull/18))
* 🖼️ Distro - Add NekOS ([dylanaraps#2186](https://github.com/dylanaraps/neofetch/pull/2186))
* 🖼️ Distro - Add astOS ([dylanaraps#2185](https://github.com/dylanaraps/neofetch/pull/2185))
* 🖼️ Distro - Fix ChromeOS identification ([dylanaraps#1949](https://github.com/dylanaraps/neofetch/pull/1949))
* 🖼️ WM - Add Hyprland to the list of wayland wms ([dylanaraps#2190](https://github.com/dylanaraps/neofetch/pull/2190))
* 🖼️ Env - Add Java, Python, Node version detection (can be enabled in config)
* 🖼️ Bug Fix - Fix hostname detection when `inetutils` is not installed
* 🖼️ Bug Fix - Fix empty brackets displayed when no theme is found ([dylanaraps#1713](https://github.com/dylanaraps/neofetch/pull/1713))
* 🖼️ Bug Fix - Fix `$` escape bug in `strip_escape_codes()` ([dylanaraps#1543](https://github.com/dylanaraps/neofetch/pull/1543))
* 🖼️ Bug Fix - Fix backslash escape bug in `strip_escape_codes()` ([dylanaraps#1543](https://github.com/dylanaraps/neofetch/pull/1543))
* 🖼️ Bug Fix - Fix CPU detection on ARM QEMU

### 1.4.0

* 🌈 Add finsexual flag (#12)
* 🚀 Addressed a total of 128 currently open pull requests from neofetch

<details>
  <summary>🖼️ Meta Changes</summary>  

* Meta - Fixed shellcheck warnings in `neowofetch`
* Meta - Moved shellcheck from travis to GitHub Actions
* Meta - Created a script to automatically generate distro list
* Colors - Allow RGB colors in neofetch `--ascii_colors` argument ([dylanaraps#1726](https://github.com/dylanaraps/neofetch/pull/1726))

</details>

<details>
  <summary>🖼️ Distro/OS Support Changes</summary>  

* Distro - Update Ubuntu logo ([dylanaraps#2125](https://github.com/dylanaraps/neofetch/pull/2125))
* Distro - Add Exodia OS Predator ([dylanaraps#2174](https://github.com/dylanaraps/neofetch/pull/2174))
* Distro - Add Parch ([dylanaraps#2045](https://github.com/dylanaraps/neofetch/pull/2045))
* Distro - Add VzLinux ([dylanaraps#1971](https://github.com/dylanaraps/neofetch/pull/1971))
* Distro - Add Twister OS ([dylanaraps#1890](https://github.com/dylanaraps/neofetch/pull/1890))
* Distro - Add BlackPantherOS ([dylanaraps#1761](https://github.com/dylanaraps/neofetch/pull/1761))
* Distro - Add TorizonCore ([dylanaraps#1744](https://github.com/dylanaraps/neofetch/pull/1744))
* Distro - Add KrassOS ([dylanaraps#1631](https://github.com/dylanaraps/neofetch/pull/1631))
* Distro - Add Synology DSM ([dylanaraps#1666](https://github.com/dylanaraps/neofetch/pull/1666))
* Distro - Add MatuusOS ([dylanaraps#1902](https://github.com/dylanaraps/neofetch/pull/1902))
* Distro - Add HarDClanZ Linux ([dylanaraps#1797](https://github.com/dylanaraps/neofetch/pull/1797))

</details>

<details>
  <summary>🖼️ Device Support Changes</summary>

* Host - Identify iMac, Mac mini, Mac Pro Models ([dylanaraps#1944](https://github.com/dylanaraps/neofetch/pull/1944))
* Host - Identify FreeBSD host model ([dylanaraps#1588](https://github.com/dylanaraps/neofetch/pull/1588))
* Font - Better font matching for st ([dylanaraps#1877](https://github.com/dylanaraps/neofetch/pull/1877))
* Theme - Use XSETTINGS to get theme without a DE ([dylanaraps#1831](https://github.com/dylanaraps/neofetch/pull/1831))
* Theme - Add QT theme detection ([dylanaraps#1713](https://github.com/dylanaraps/neofetch/pull/1713))
* Theme - Add LeftWM theme detection ([dylanaraps#1963](https://github.com/dylanaraps/neofetch/pull/1963))
* Cursor - Add cursor theme detection ([dylanaraps#1149](https://github.com/dylanaraps/neofetch/pull/1149))
* Terminal - Improve NixOS terminal identification ([dylanaraps#1134](https://github.com/dylanaraps/neofetch/pull/1134))
* Terminal - Use `/proc/.../cmdline` instead of `.../comm` ([dylanaraps#2034](https://github.com/dylanaraps/neofetch/pull/2034))
* Packages - Improve scoop/choco package count ([dylanaraps#1642](https://github.com/dylanaraps/neofetch/pull/1642))

</details>

<details>
  <summary>🖼️ Bug Fixes</summary>

* Bug Fix - Fix prepended `=` for kitty ([dylanaraps#2116](https://github.com/dylanaraps/neofetch/pull/2116))
* Bug Fix - Hide domain in hostname by default ([dylanaraps#2095](https://github.com/dylanaraps/neofetch/pull/2095))
* Bug Fix - Respect TMPDIR if it exists ([dylanaraps#1891](https://github.com/dylanaraps/neofetch/pull/1891))
* Bug Fix - Fix terminal size over slow connection ([dylanaraps#1895](https://github.com/dylanaraps/neofetch/pull/1895))
* Bug Fix - Fix GPU detection for bumblebee dual-GPU ([dylanaraps#1131](https://github.com/dylanaraps/neofetch/pull/1131))
* Bug Fix - Strip colors in ASCII length calculation ([dylanaraps#1543](https://github.com/dylanaraps/neofetch/pull/1543))

</details>

### 1.3.0

<details>
  <summary>🖼️ Ascii Art Changes</summary>  

* Ascii - Improve Trisquel ([dylanaraps#1946](https://github.com/dylanaraps/neofetch/pull/1946))
* Ascii - Improve LangitKetujuh ([dylanaraps#1948](https://github.com/dylanaraps/neofetch/pull/1948))
* Ascii - Improve Artix small ([dylanaraps#1872](https://github.com/dylanaraps/neofetch/pull/1872))
* Ascii - Update Archcraft ([dylanaraps#1919](https://github.com/dylanaraps/neofetch/pull/1919))

</details>

<details>
  <summary>🖼️ Distro/OS Support Changes</summary>  

* OS - Support Old macOS 10.4 and 10.5 ([dylanaraps#2151](https://github.com/dylanaraps/neofetch/pull/2151))
* OS - Identify Hackintosh VM ([dylanaraps#2005](https://github.com/dylanaraps/neofetch/pull/2005))
* Distro - Fix model detection for Ubuntu Touch ([dylanaraps#2167](https://github.com/dylanaraps/neofetch/pull/2167))
* Distro - Add EncryptOS ([dylanaraps#2158](https://github.com/dylanaraps/neofetch/pull/2158))
* Distro - Add BigLinux ([dylanaraps#2061](https://github.com/dylanaraps/neofetch/pull/2061))
* Distro - Add AmogOS ([dylanaraps#1904](https://github.com/dylanaraps/neofetch/pull/1904))
* Distro - Add CutefishOS ([dylanaraps#2054](https://github.com/dylanaraps/neofetch/pull/2054))
* Distro - Add PearOS ([dylanaraps#2049](https://github.com/dylanaraps/neofetch/pull/2049))
* Distro - Add FusionX ([dylanaraps#2011](https://github.com/dylanaraps/neofetch/pull/2011))
* Distro - Add Q4OS ([dylanaraps#1973](https://github.com/dylanaraps/neofetch/pull/1973))
* Distro - Add CachyOS ([dylanaraps#2026](https://github.com/dylanaraps/neofetch/pull/2026))
* Distro - Add Soda Linux ([dylanaraps#2023](https://github.com/dylanaraps/neofetch/pull/2023))
* Distro - Add Elive Linux ([dylanaraps#1957](https://github.com/dylanaraps/neofetch/pull/1957))
* Distro - Add Uos ([dylanaraps#1991](https://github.com/dylanaraps/neofetch/pull/1991))
* Distro - Add MassOS ([dylanaraps#1947](https://github.com/dylanaraps/neofetch/pull/1947))
* Distro - Add CalinixOS ([dylanaraps#1988](https://github.com/dylanaraps/neofetch/pull/1988))
* Distro - Add Kaisen Linux ([dylanaraps#1958](https://github.com/dylanaraps/neofetch/pull/1958))
* Distro - Add yiffOS ([dylanaraps#1920](https://github.com/dylanaraps/neofetch/pull/1920))
* Distro - Add Sulin ([dylanaraps#1896](https://github.com/dylanaraps/neofetch/pull/1896))
* Distro - Add Wii Linux ([dylanaraps#1929](https://github.com/dylanaraps/neofetch/pull/1929))
* Distro - Add Linspire ([dylanaraps#1905](https://github.com/dylanaraps/neofetch/pull/1905))
* Distro - Add Ubuntu Kylin ([dylanaraps#1974](https://github.com/dylanaraps/neofetch/pull/1974))
* Distro - Add OPNsense ([dylanaraps#1055](https://github.com/dylanaraps/neofetch/pull/1055))
* Distro - Improve BSD machine arch detection ([dylanaraps#2015](https://github.com/dylanaraps/neofetch/pull/2015))
* Distro - Improve Manjaro version detection ([dylanaraps#1879](https://github.com/dylanaraps/neofetch/pull/1879))

</details>

<details>
  <summary>🖼️ Device Support Changes</summary>  

* Terminal - Add Fig ([dylanaraps#2077](https://github.com/dylanaraps/neofetch/pull/2077))
* Terminal - Identify font for Apple Terminal ([dylanaraps#2017](https://github.com/dylanaraps/neofetch/pull/2017))
* CPU - Identify core count for Apple M1 ([dylanaraps#2038](https://github.com/dylanaraps/neofetch/pull/2038))
* GPU - Identify OpenCL GPU without PCIe ([dylanaraps#1928](https://github.com/dylanaraps/neofetch/pull/1928))
* Host - Identify MacBook & Update iDevice models ([dylanaraps#1944](https://github.com/dylanaraps/neofetch/pull/1944))
* Battery - Identify power adapter for MacBooks ([dylanaraps#1945](https://github.com/dylanaraps/neofetch/pull/1945))
* DE - Identify KF5 and Qt versions for Plasma ([dylanaraps#2019](https://github.com/dylanaraps/neofetch/pull/2019))
* Packages - Improve GUIX package detection ([dylanaraps#2021](https://github.com/dylanaraps/neofetch/pull/2021))
* Packages - Add `pm` and `cargo` ([dylanaraps#1876](https://github.com/dylanaraps/neofetch/pull/1876))
* Network - Identify network capabilities ([dylanaraps#1511](https://github.com/dylanaraps/neofetch/pull/1511))

</details>

<details>
  <summary>🖼️ Bug Fixes</summary>

* Bug Fix - Fix `col_offset` ([dylanaraps#2042](https://github.com/dylanaraps/neofetch/pull/2042))
* Bug Fix - Prioritize `/etc/os-release` ([dylanaraps#2067](https://github.com/dylanaraps/neofetch/pull/2067))
* Bug Fix - Ignore case when counting `.appimage` ([dylanaraps#2006](https://github.com/dylanaraps/neofetch/pull/2006))
* Bug Fix - Fix BSD freezing if pkg is not bootstrapped ([dylanaraps#2014](https://github.com/dylanaraps/neofetch/pull/2014))
* Bug Fix - Fix wrong icon theme ([dylanaraps#1873](https://github.com/dylanaraps/neofetch/pull/1873))

</details>

### 1.2.0

* 🚀 Take over `neofetch` with `neowofetch`

<details>
  <summary>🖼️ Ascii Art Changes</summary>

* Ascii - Add uwuntu ([#9](https://github.com/hykilpikonna/hyfetch/pull/9)) (use it with `hyfetch --test-distro uwuntu` or `neowofetch --ascii_distro uwuntu`)
* Ascii - Better Void ascii art ([#10](https://github.com/hykilpikonna/hyfetch/pull/10))
* Ascii - Update old NixOS logo for compatibility ([dylanaraps#2114](https://github.com/dylanaraps/neofetch/pull/2114))

</details>

<details>
  <summary>🖼️ Distro/OS Support Changes</summary>

* OS - Identify macOS 13 Ventura ([#8](https://github.com/hykilpikonna/hyfetch/pull/8))
* OS - Windows 11 Fluent ([dylanaraps#2109](https://github.com/dylanaraps/neofetch/pull/2109))
* Distro - Add Asahi Linux ([dylanaraps#2079](https://github.com/dylanaraps/neofetch/pull/2079))
* Distro - Add CenterOS ([dylanaraps#2097](https://github.com/dylanaraps/neofetch/pull/2097))
* Distro - Add Finnix ([dylanaraps#2099](https://github.com/dylanaraps/neofetch/pull/2099))
* Distro - Add Miracle Linux ([dylanaraps#2085](https://github.com/dylanaraps/neofetch/pull/2085))
* Distro - Add Univalent ([dylanaraps#2162](https://github.com/dylanaraps/neofetch/pull/2162))
* Distro - Add NomadBSD ([dylanaraps#2147](https://github.com/dylanaraps/neofetch/pull/2147))
* Distro - Add GrapheneOS ([dylanaraps#2146](https://github.com/dylanaraps/neofetch/pull/2146))
* Distro - Add ShastraOS ([dylanaraps#2149](https://github.com/dylanaraps/neofetch/pull/2149))
* Distro - Add Ubuntu Touch ([dylanaraps#2167](https://github.com/dylanaraps/neofetch/pull/2167))
* Distro - Add Ubuntu Sway ([dylanaraps#2136](https://github.com/dylanaraps/neofetch/pull/2136))
* Distro - Add Orchid Linux ([dylanaraps#2144](https://github.com/dylanaraps/neofetch/pull/2144))
* Distro - Add AOSC OS/Retro ([dylanaraps#2124](https://github.com/dylanaraps/neofetch/pull/2124))
* Distro - Add Ultramarine Linux ([dylanaraps#2115](https://github.com/dylanaraps/neofetch/pull/2115))
* Distro - Improve NixOS version detection ([dylanaraps#2157](https://github.com/dylanaraps/neofetch/pull/2157))

</details>

<details>
  <summary>🖼️ Device/Program Support Changes</summary>

* Terminal - Add Termux ([dylanaraps#1923](https://github.com/dylanaraps/neofetch/pull/1923))
* CPU - Add loongarch64 ([dylanaraps#2140](https://github.com/dylanaraps/neofetch/pull/2140))
* CPU - Identify CPU name for ARM / RISCV ([dylanaraps#2139](https://github.com/dylanaraps/neofetch/pull/2139))
* Battery - Fix file not found ([dylanaraps#2130](https://github.com/dylanaraps/neofetch/pull/2130))
* GPU - Identify open-kernal Nvidia driver version ([dylanaraps#2128](https://github.com/dylanaraps/neofetch/pull/2128))

</details>

<details>
  <summary>🖼️ Bug Fixes</summary>

* Bug Fix - Fix broken fedora output ([dylanaraps#2084](https://github.com/dylanaraps/neofetch/pull/2084))

</details>

<img width="200px" src="https://user-images.githubusercontent.com/22280294/181790059-47aa6f80-be99-4e67-8fa5-5c02b02842c6.png" align="right">

### 1.1.3rc1

* 🌈 Add foreground-background color arrangement to make Fedora and Ubuntu look nicer
* 🌈 Allow typing abbreviations in flag selection
* 🌈 Fix: Duplicate random color arrangements are appearing in selection screen
* 🌈 Fix: Inconsistant color arrangement when saved to config file

### 1.1.2

* Add more flags ([#5](https://github.com/hykilpikonna/hyfetch/pull/5))
* Removed `numpy` dependency that was used in 1.1.0

<img width="200px" src="https://user-images.githubusercontent.com/22280294/180901539-014f036e-c926-4470-ac72-a6d6dcf30672.png" align="right">

### 1.1.0

* Refactored a lot of things
* Added Beiyang flag xD
* Added interactive configurator for brightness adjustment
* Added dark/light mode selection
* Added color bar preview for RGB/8bit mode selection
* Added random color arrangement feature (for NixOS)

### 1.0.7

* Fix: Make config path not on init but when it's actually needed.

### 1.0.6

* Remove `hypy_utils` dependency to make packaging easier.

### 1.0.5

* Fix terminal emulator detection ([PR #2](https://github.com/hykilpikonna/hyfetch/pull/2))

### 1.0.4

* Add more flags ([PR #1](https://github.com/hykilpikonna/hyfetch/pull/1))

### 1.0.3

* Fix missing dependency for setuptools

### 1.0.2

* Implement RGB to 8bit conversion
* Add support for Python 3.7 and 3.8

### 1.0.1

* Included 11 flag presets
* Ability to lighten colors with `--c-set-l <lightness>`
* Command-line flag chooser
* Supports Python >= 3.9

## More Screenshots

![image](https://user-images.githubusercontent.com/22280294/162614578-3b878abb-2a32-4427-997e-f90b3f5cfd7c.png)
![image](https://user-images.githubusercontent.com/22280294/162661621-f1c61338-7857-4d3f-9fe3-c6b635d68c38.png)

## Original Readme from Neofetch Below

<h3 align="center"><img src="https://i.imgur.com/ZQI2EYz.png" alt="logo" height="100px"></h3>
<p align="center">A command-line system information tool written in bash 3.2+</p>

<p align="center">
<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
<a href="https://github.com/dylanaraps/neofetch/releases"><img src="https://img.shields.io/github/release/dylanaraps/neofetch.svg"></a>
<a href="https://repology.org/metapackage/neofetch"><img src="https://repology.org/badge/tiny-repos/neofetch.svg" alt="Packaging status"></a>
</p>

<img src="https://i.imgur.com/GFmC5Ad.png" alt="neofetch" align="right" height="240px">

Neofetch is a command-line system information tool written in `bash 3.2+`. Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.

The overall purpose of Neofetch is to be used in screen-shots of your system. Neofetch shows the information other people want to see. There are other tools available for proper system statistic/diagnostics.

The information by default is displayed alongside your operating system's logo. You can further configure Neofetch to instead use an image, a custom ASCII file, your wallpaper or nothing at all.

<img src="https://i.imgur.com/lUrkQBN.png" alt="neofetch" align="right" height="240px">

You can further configure Neofetch to display exactly what you want it to. Through the use of command-line flags and the configuration file you can change existing information outputs or add your own custom ones.


Neofetch supports almost 150 different operating systems. From Linux to Windows, all the way to more obscure operating systems like Minix, AIX and Haiku. If your favourite operating system is unsupported: Open up an issue and support will be added.


### More: \[[Dependencies](https://github.com/dylanaraps/neofetch/wiki/Dependencies)\] \[[Installation](https://github.com/dylanaraps/neofetch/wiki/Installation)\] \[[Wiki](https://github.com/dylanaraps/neofetch/wiki)\]
