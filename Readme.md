# fetch.sh

## Big updates: Check the releases page.

This is the home of my fetch script! This script gathers info <br\>
about your system and prints it to the terminal.

If you're having any issues or have any ideas, please open an issue! <br\>
I can't test on many other distros and I want this to work <br\>
for as many people as possible.

![1](https://sr.ht/Jd8Y.png)


<!-- {{{ -->


## Dependencies

These are the script's required dependencies

-  Text formatting, dynamic image size and padding: tput

These are the script's optional dependencies:

-  Displaying Images: w3m
-  Image Cropping: ImageMagick
-  Display Wallpaper: feh
-  Current Song: mpc
-  Resolution Detection: xorg-xdpyinfo


<!-- }}} -->


<!-- {{{ -->


## Usage

The script now supports dynamic image sizing and padding,
<br\> it's enabled by default and there's a variable you
<br\> need to set for it to work correctly.

You can either change the variable $fontwidth inside of the
<br\> script or launch it with ```--font_width num```.

Once you set the var the script will scale the image and padding
<br\> to fit your terminal window.

Please report any bugs or issues you're having with this as I can't
<br\> test with many configurations.


```
usage: scrot.sh [--colors 1 2 4 5] [--kernel "$(uname -rs)"]

Info:
--title string         Change the title at the top
--distro string/cmd    Manually set the distro
--kernel string/cmd    Manually set the kernel
--uptime string/cmd    Manually set the uptime
--uptime_shorthand on/off --v
                       Shorten the output of uptime
--packages string/cmd  Manually set the package count
--shell string/cmd     Manually set the shell
--winman string/cmd    Manually set the window manager
--cpu string/cmd       Manually set the cpu name
--memory string/cmd    Manually set the memory
--speed_type           Change the type of cpu speed to get
                       Possible values: current, min, max
--song string/cmd      Manually set the current song

Text Colors:
--colors 1 2 3 4 5      Change the color of text
                       (title, subtitle, colon, info)
--title_color num      Change the color of the title
--subtitle_color num   Change the color of the subtitle
--colon_color num      Change the color of the colons
--underline_color num  Change the color of the underline
--info_color num       Change the color of the info

Text Formatting:
--underline on/off     Enable/Disable title underline
--underline_char char  Character to use when underlineing title
--line_wrap on/off     Enable/Disable line wrapping
--bold on/off          Enable/Disable bold text

Color Blocks:
--color_blocks on/off  Enable/Disable the color blocks
--block_range start end --v
                        Range of colors to print as blocks
--block_width num       Width of color blocks

Image:
--image                Image to display with the script
                       The image gets priority over other
                       images: (wallpaper, \$img)

--font_width px        Used to automatically size the image
--image_position       Where to display the image: (Left/Right)
--split_size num       Width of img/text splits
                       A value of 2 makes each split half the terminal
                       width and etc
--crop_mode            Which crop mode to use
                       Takes the values: normal, fit, fill
--crop_offset value    Change the crop offset for crop_mode normal.
                       Possible values: northwest, north, northeast,
                       west, center, east, southwest, south, southeast
--xoffset px           How close the image will be
                       to the left edge of the window
--yoffset px           How close the image will be
                       to the top edge of the window

--gap num              Gap between image and text right side
--images on/off        Enable/Disable all images
--wall on/off          Enable/Disable the wallpaper function
                       and fallback to \$img
--clean                Remove all cropped images

Other:
--help                 Print this text and exit
```


<!-- }}} -->


<!-- {{{ -->


## TODO

Here's what's on my todo list

- Uptime doesn't work in OS X yet.

- Windows support (I'm almost done)

- OpenBSD support (Partially implemented, just needs testing)

- Imagemagick optimizations

- Cleanup of info array handling

- More info outputs. Now that it's easy to customize what's printed and
  everything is a function we can add optional support for pretty much anything.

    - Resolution
    - GTK themes
    - Terminal Font
    - GPU
    - IP
    - etc

<!-- }}} -->


### Crop mode comparison

#### Fit
![fit](https://imgur.com/MI0UtSV.png)

#### Fill
![fill](https://imgur.com/LvxYwki.png)


### Thanks

Thanks to:

- Screenfetch: I've used some snippets as a base for a few functions in this script

- @jrgz: Helping me test the Mac OS X version.
