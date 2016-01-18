# fetch

[[Features](#features)]  [[Dependencies](#dependencies)]  [[Installation](#installation)]  [[Post Install](#post-install)]  [[Usage](#usage)] [[Issues and Workarounds](#issues-and-workarounds)]  [[TODO](#todo)]  [[Thanks](#thanks)]

This is the home of my fetch script! This script gathers info <br />
about your system and prints it to the terminal next to an image of your choice!


![1](http://i.imgur.com/bORHxT5.png)


<!-- Features {{{ -->


## Features


- **Supports Linux, Mac OS X, \*BSD and Windows (Cygwin)!**
    - If the script isn't working on your system open an issue.
        - *BSD support is currently in testing! See issue [#10](https://github.com/dylanaraps/fetch/issues/10#issuecomment-172432389)
- **It's Fast**
    - The script makes heavy use of bash builtins and <br \>string manipulation.
- **Display an image next to the info. (or don't!)**
    - The script can use your current wallpaper, shuffle through a directory or just <br \>display an image of your choice.
        - The wallpaper function on linux uses feh, It's hard to add support <br \>
          for other wallpaper setters as they don't provide a way of getting <br \>
          the current wallpaper from the cli.
- **Highly Customizable**
    - You can customize almost everything.
        - See Usage below or lines 23-233 in script
- **Take a screenshot at the end.**
    - It's disabled by default and you can specify the cmd <br \>to use with `--scrotcmd cmd` at launch or by <br \>changing the value of `$scrotcmd` in the script.
- **Smart crop (or Waifu crop)**
    - See https://github.com/dylanaraps/fetch/wiki/What-is-Smart-Crop%3F


<!-- }}} -->


<!-- Dependences {{{ -->


## Dependencies


#### Required dependencies:

-  Bash **4.0+**
-  Text formatting, dynamic image size and padding: `tput`
-  Uptime detection: `procps` or `procps-ng`

#### Optional dependencies:

All OS:

-  Displaying Images: `w3m`
    - You may also need `w3m-img`
-  Image Cropping, Resizing etc: `ImageMagick`
-  Current Song: `mpc`
-  Resolution Detection: `xorg-xdpyinfo`
-  Window manager detection: `wmctrl`
    - This is used as a fallback to parsing `.xinitrc` and `$XDG_CURRENT_DESKTOP`.
-  Take a screenshot on script finish: `scrot`
    - You can change this to another program with a `--scrotcmd` and an in script option.

Linux | \*BSD:

-  Display Wallpaper: `feh`


<!-- }}} -->


<!-- Installation {{{ -->


## Installation


### Arch

1. Install `fetch-git` from the aur.


### Others

1. Download the latest source at https://github.com/dylanaraps/fetch
2. Make the file executable using chmod. `chmod +x /path/to/fetch`
3. Move the script to somewhere in your $PATH or just run it from where it is.


<!-- }}} -->


<!-- Post Install {{{ -->

## Post Install


**NOTE:** For the images to be sized correctly you need to set the `$font_width` variable.
If you don't know your font width in pixels keep trying values until the image is sized correctly.

You can also use the launch flag `--font_width` to set it on the fly.

You can customize what info to print by editing the info array near the top of the script.
The array looks like this:

```sh
info=(
    "gettitle"
    "underline"
    "OS: getdistro"
    "Kernel: getkernel"
    "Uptime: getuptime"
    "Packages: getpackages"
    etc...
)
```

See these comments inside the script for more info:
https://github.com/dylanaraps/fetch/blob/master/fetch#L29

If you don't want to edit the script you can customize everything using flags at launch!

Here's what my fetch alias looks like:

```sh
alias fetch2="fetch \
--block_range 1 8 \
--line_wrap off \
--bold off \
--uptime_shorthand on \
--gtk_shorthand on \
--exclude 'Icons: getgtkicons' \
--exclude 'Resolution: getresolution' \
--colors 4 1 8 8 8 7 \
"
```

<!-- }}} -->


<!-- Usage {{{ -->


## Usage


    usage: ${0##*/} [--colors 1 2 3 4 5] [--kernel "\$\(uname -rs\)"]

    Info:
    --exclude "OS: getos"  Disable an info line at launch
    --title string         Change the title at the top
    --distro string/cmd    Manually set the distro
    --kernel string/cmd    Manually set the kernel
    --uptime string/cmd    Manually set the uptime
    --uptime_shorthand on/off --v
                           Shorten the output of uptime
    --packages string/cmd  Manually set the package count
    --shell string/cmd     Manually set the shell
    --winman string/cmd    Manually set the window manager
    --use_wmctrl on/off    Use wmctrl for a more accurate reading
    --gtk_shorthand on/off Shorten output of gtk theme/icons
    --cpu string/cmd       Manually set the cpu name
    --memory string/cmd    Manually set the memory
    --speed_type           Change the type of cpu speed to get
                           Possible values: current, min, max
    --song string/cmd      Manually set the current song

    Text Colors:
    --colors 1 2 3 4 5     Change the color of text
                           (title, subtitle, colon, underline, info)
    --title_color num      Change the color of the title
    --subtitle_color num   Change the color of the subtitle
    --colon_color num      Change the color of the colons
    --underline_color num  Change the color of the underlines
    --info_color num       Change the color of the info

    Text Formatting:
    --underline on/off     Enable/Disable title underline
    --underline_char char  Character to use when underlineing title
    --line_wrap on/off     Enable/Disable line wrapping
    --bold on/off          Enable/Disable bold text
    --prompt_height num    Set this to your prompt height to fix
                           issues with the text going off screen at the top

    Color Blocks:
    --color_blocks on/off  Enable/Disable the color blocks
    --block_width num      Width of color blocks
    --block_range start end --v
                           Range of colors to print as blocks

    Image:
    --image                Image source. Where and what image we display.
                           Possible values: wall, shuffle, /path/to/img, off
    --shuffledir           Which directory to shuffle for an image.
    --font_width px        Used to automatically size the image
    --image_position       Where to display the image: (Left/Right)
    --split_size num       Width of img/text splits
                           A value of 2 makes each split half the terminal
                           width and etc
    --crop_mode            Which crop mode to use
                           Takes the values: normal, fit, fill
    --crop_offset value    Change the crop offset for normal mode.
                           Possible values: northwest, north, northeast,
                           west, center, east, southwest, south, southeast

    --xoffset px           How close the image will be
                           to the left edge of the window
    --yoffset px           How close the image will be
                           to the top edge of the window
    --gap num              Gap between image and text right side
                           to the top edge of the window
    --clean                Remove all cropped images

    Screenshot:
    --scrot                Take a screenshot
    --scrotdir             Directory to save the scrot
    --scrotfile            File name of scrot
    --scrotcmd             Screenshot program to launch

    Other:
    --clear on/off         Whether or not to clear the terminal
                           before printing.
    --help                 Print this text and exit


<!-- }}} -->


<!-- Issues and Workarounds {{{ -->


## Issues and Workarounds


#### The image is rendering with black lines in Urxvt while using an xft font.

This is an issue with w3mimgdisplay and not the script. You can find a workaround here:

https://github.com/hut/ranger/issues/86#issuecomment-17346249


#### The text is too long for my terminal window and wraps to the next line causing the image to not render correctly.

There are a few ways to fix this.

* Disable line wrapping with `$line_wrap off` in the script or with the launch flag `--line_wrap off`

* The uptime and gtk info lines each have a shorthand option that makes their output smaller. You can <br \>
  enable them by changing these variables or using these flags.

```sh
# In script options
$uptime_shorthand on
$gtk_shorthand on

# Launch flags
--uptime_shorthand on
--gtk_shorthand on
```

* Edit the info array to make the subtitles shorter

* Resizing the terminal so that the lines don't wrap.


#### [Linux] The script hangs and doesn't display anything

This is caused by the getwallpaper function failing to find your current wallpaper and <br \>
imagemagick trying to crop a nonexistent image. You can fix this by installing feh and using it<br \>
to set your wallpaper or by changing the image source.

You can change the source by editing the `$image` variable or by launching the script with `--image`.

The possible values are:

* **wall** - Use the current wallpaper. (Default)
* **shuffle** - Shuffle through images in a directory. See `$shuffledir`
* **path/to/img.png** - Select an image to display.
* **off** - Disable images


<!-- }}} -->


<!-- TODO {{{ -->


## TODO

Here's what's on my todo list

- Add Windows resolution detection

- Add BSD cpu speed

- Look into iterm2 image rendering

- Cleanup of info array handling

- Imagemagick optimizations

- More info outputs. Now that it's easy to customize what's printed and<br \>
  everything is a function we can add optional support for pretty much anything.

    - Resolution (Done!)
    - GTK themes (Done!)
    - Terminal Font
    - GPU
    - IP
    - etc


<!-- }}} -->


<!-- Thanks {{{ -->


## Thanks

Thanks to:

- metakirby5: Providing great feedback as well as ideas for the script.

- Screenfetch: I've used some snippets as a base for a few functions in this script.

- @jrgz: Helping me test the Mac OS X version.

- @xDemonessx: Helping me test the Windows version.


<!-- }}} -->
