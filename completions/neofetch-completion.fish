# neofetch.fish
# Completion file for the neofetch tool.

# Inititate {{{

# Extract options from the manual
function __neofetch_options
  neofetch --help | awk '/^[[:space:]]+--?/{ sub(/\,/, ""); print $1 }'
end

# Supplement the completion with the extract
complete -f -c neofetch -a '(__neofetch_options)'

# TODO: Hack to make it directly complete with '--'. Also don't show
# folders directly when beginning tabbing.

# }}}

# Functions {{{
function __neofetch_ascii_distro
  echo -en"aix
alpine
alpine_small
amazon
anarchy
android
antergos
antix
aosc
apricity
arch
arch_old
arch_small
archbox
archlabs
archmerge
arcolinux
artix
arya
bitrig
blag
blankon
bsd
bunsenlabs
calculate
centos
chakra
chaletos
chapeau
chrom
clover
condres
crux
crux_small
darwin
debian
debian_small
deepin
desaos
devuan
dracos
dragonfly
dragonfly_old
dragonfly_small
elementary
endless
exherbo
fedora
freebsd
freebsd_small
freemint
frugalware
funtoo
galliumos
gentoo
gentoo_small
gnewsense
gnu
gobolinux
grombyang
guixsd
haiku
hyperbola
irix
kali
kaos
kde
kibojoe
kogaion
korora
kslinux
kubuntu
lede
linux lite
linux mint
linux
lmde
lubuntu
lunar
mac
mageia
magpieos
manjaro
maui
mer
minix
mx
netbsd
netrunner
nitrux
nixos
nixos_small
nurunner
nutyx
obrevenge
open source media center
openbsd
openbsd_small
openindiana
openmandriva
opensuse
openwrt
oracle
pacbsd
parabola
pardus
parrot
parsix
pcbsd
pclinuxos
peppermint
porteus
postmarketos
puppy
pureos
qubes
raspbian
red star
redcore
redcore
redhat
regata
rosa
sabayon
sabotage
sailfishos
salentos
scientific
sharklinux
siduction
slackware
slitaz
smartos
solus
sparky
steamos
sunos
swagarch
tails
trisquel
ubuntu
ubuntu_old
void
void_small
windows 10
windows
xferience
xubuntu
zorin
"
end

function __neofetch_cpu_cores
  echo -en "logical
off
physical"
end

function __neofetch_cpu_temperature
  echo -en "C
F
off"
end

function __neofetch_disk_subtitle
  echo -en "dir\t(/, Disc, etc.)
mount\t(/, /mnt/Local Disk, etc.)
name\t(sda1, sda2, etc.)
"
end

function __neofetch_display_mode
  echo -en "bar
barinfo
infobar
off
"
end

function __neofetch_gpu_type
  echo -en "all
dedicated
integrated
"
end

function __neofetch_image_backend
  echo -en "ascii
caca
iterm2
jp2a
kitty
pixterm
sixel
termpix
tycat
w3m
off
"
end

function __neofetch_image_crop_mode
  echo -en "fill
fit
normal
"
end

function __neofetch_image_crop_offset
  echo -en "center
north
northeast
east
southeast
south
southwest
west
northwest
"
end

function __neofetch_image_size
  echo -en "auto
00px
00%
none"
end

function __neofetch_image_source
  echo -en "ascii
auto
wallpaper
"
end

function __neofetch_music_player
  echo -en "amarok
audacious
banshee
bluemindo
clementine
cmus
deadbeef
deepin-music
elisa
exaile
gmusicbrowser
gnome-music
gmusicbrowser
Google Play
guayadeque
iTunes
juk
lollypop
mocp
mopidy
mpd
pogo
pragha
qmmp
quodlibet
rhythmbox
sayonara
spotify
tomahawk
vlc
xmms2d
yarock
"
end

function __neofetch_on_off
  echo -en "
off\t Turn off
on\t Turn on
"
end

function __neofetch_speed_type
  echo -en "bios
current
max
min
scaling_current
scaling_max
scaling_min
"
end

# }}}

# Info {{{
complete -x -c neofetch -l 'disable' -d 'Disable a line from the output'
complete -x -c neofetch -l 'package_managers' -a '(__neofetch_on_off)' -d 'Hide/Show package manager'
complete -x -c neofetch -l 'os_arch' -a '(__neofetch_on_off)' -d 'Hide/Show OS architecture'
complete -x -c neofetch -l 'speed_type' -a '(__neofetch_speed_type)' -d 'Change the type of CPU speed to display'
complete -x -c neofetch -l 'speed_shorthand' -a '(__neofetch_on_off)' -d 'Show decimals in CPU speed'
complete -x -c neofetch -l 'cpu_brand' -a '(__neofetch_on_off)' -d 'Enable/disable CPU brand in output'
complete -x -c neofetch -l 'cpu_cores' -a '(__neofetch_cpu_cores)' -d 'Display CPU cores'
complete -x -c neofetch -l 'cpu_speed' -a '(__neofetch_on_off)' -d 'Hide/Show CPU speed'
complete -x -c neofetch -l 'cpu_temp' -a '(__neofetch_cpu_temperature)' -d 'Hide/Show CPU temperature'
complete -x -c neofetch -l 'distro_shorthand' -a '(__neofetch_on_off)' -d 'Shorten the output of distro'
complete -x -c neofetch -l 'kernel_shorthand' -a '(__neofetch_on_off)' -d 'Shorten the output of kernel'
complete -x -c neofetch -l 'uptime_shorthand' -a '(__neofetch_on_off)' -d 'Shorten the output of uptime'
complete -x -c neofetch -l 'refresh_rate' -a '(__neofetch_on_off)' -d 'Hide/Show refresh rate of each monitor'
complete -x -c neofetch -l 'gpu_brand' -a '(__neofetch_on_off)' -d 'Hide/Show GPU brand'
complete -x -c neofetch -l 'gpu_type' -a '(__neofetch_gpu_type)' -d 'Select which GPU to show'
complete -x -c neofetch -l 'gtk_shorthand' -a '(__neofetch_on_off)' -d 'Shorten output of GTK theme'
complete -x -c neofetch -l 'gtk2' -a '(__neofetch_on_off)' -d 'Hide/Show GTK2 theme/font/icons output'
complete -x -c neofetch -l 'gtk3' -a '(__neofetch_on_off)' -d 'Hide/Show GTK3 theme/font/icons output'
complete -x -c neofetch -l 'shell_path' -a '(__neofetch_on_off)' -d 'Hide/Show $SHELL path'
complete -x -c neofetch -l 'shell_version' -a '(__neofetch_on_off)' -d 'Hide/Show $SHELL version'
complete -x -c neofetch -l 'disk_show' -d 'Whick disk to show'
complete -x -c neofetch -l 'disk_subtitle' -a '(__neofetch_disk_subtitle)' -d 'Append to disk subtitle'
complete -x -c neofetch -l 'ip_host' -d 'URL to query for public IP'
complete -x -c neofetch -l 'song_format' -d 'Song data in specific data'
complete -x -c neofetch -l 'song_shorthand' -a '(__neofetch_on_off)' -d 'Print song on separate lines'
complete -x -c neofetch -l 'music_player' -a '(__neofetch_music_player)' -d 'Manually select a music player'

# }}}
# Text {{{

complete -x -c neofetch -l 'colors' -d 'Change text colors. Check manual'
complete -x -c neofetch -l 'underline' -a '(__neofetch_on_off)' -d 'Hide/Show the underline'
complete -x -c neofetch -l 'underline_char' -d 'Character to use when underlining title'
complete -x -c neofetch -l 'bold' -a '(__neofetch_on_off)' -d 'Hide/Show bold text'

# }}}
# Color {{{

complete -x -c neofetch -l 'color_blocks' -a '(__neofetch_on_off)' -d 'Hide/Show color blocks'
complete -x -c neofetch -l 'block_width' -d 'Width of color blocks in spaces'
complete -x -c neofetch -l 'block_height' -d 'Height of color blocks in spaces'
complete -x -c neofetch -l 'block_range' -d 'Range of colors to print as blocks'

# }}}
# Bars {{{

complete -x -c neofetch -l 'bar_char' -d 'Characters to use when drawing bars'
complete -x -c neofetch -l 'bar_border' -a '(__neofetch_on_off)' -d 'Surround the bar with \'[]\''
complete -x -c neofetch -l 'bar_length' -d 'Length in spaces to make bars'
complete -x -c neofetch -l 'bar_colors' -d 'Colors to make the bar'
complete -x -c neofetch -l 'cpu_display' -a '(__neofetch_display_mode)' -d 'CPU bar mode'
complete -x -c neofetch -l 'memory_display' -a '(__neofetch_display_mode)' -d 'Memory bar mode'
complete -x -c neofetch -l 'battery_display' -a '(__neofetch_display_mode)' -d 'Batter bar mode'
complete -x -c neofetch -l 'disk_display' -a '(__neofetch_display_mode)' -d 'Disk bar mode'

# }}}
# Image Backend {{{

complete -x -c neofetch -l 'backend' -a '(__neofetch_image_backend)' -d 'Select backend'
complete -r -c neofetch -l 'source' -a '(__neofetch_image_source)' -d 'Select image source'
complete -r -c neofetch -l 'ascii' -a '(__neofetch_image_source)' -d 'ASCII backend'
complete -r -c neofetch -l 'caca' -a '(__neofetch_image_source)' -d 'caca backend'
complete -r -c neofetch -l 'iterm2' -a '(__neofetch_image_source)' -d 'iTerm2 backend'
complete -r -c neofetch -l 'jp2a' -a '(__neofetch_image_source)' -d 'jp2a backend'
complete -r -c neofetch -l 'kitty' -a '(__neofetch_image_source)' -d 'Kitty backend'
complete -r -c neofetch -l 'pixterm' -a '(__neofetch_image_source)' -d 'pixterm backend'
complete -r -c neofetch -l 'sixel' -a '(__neofetch_image_source)' -d 'sixel backend'
complete -r -c neofetch -l 'termpix' -a '(__neofetch_image_source)' -d 'termpix backend'
complete -r -c neofetch -l 'tycat' -a '(__neofetch_image_source)' -d 'tycat backend'
complete -r -c neofetch -l 'w3m' -a '(__neofetch_image_source)' -d 'w3m backend'
complete -f -c neofetch -l 'off' -d 'Disable ASCII art'

# }}}
# ASCII {{{

complete -x -c neofetch -l 'ascii_colors' -d 'Colors to print the ASCII art'
complete -x -c neofetch -l 'ascii_distro' -a '(__neofetch_ascii_distro)' -d 'Which distro\'s ASCII art'
complete -x -c neofetch -l 'ascii_bold' -a '(__neofetch_on_off)' -d 'Hide/Show ASCII logo'
complete -f -c neofetch -l 'logo' -s 'L' -d 'Hide text, show onlo ASCII art'

# Image {{{

complete -f -c neofetch -l 'loop' -d 'Redraw image until CTRL+C'
complete -x -c neofetch -l 'size' -a '(__neofetch_image_size)' -d 'How to size image'
complete -x -c neofetch -l 'crop_mode' -a '(__neofetch_image_crop_mode)' -d 'Crop mode'
complete -x -c neofetch -l 'crop_offset' -a '(__neofetch_image_crop_offset)' -d 'Change crop mode in normal mode'
complete -x -c neofetch -l 'xoffset' -d 'Offset in px, left edge'
complete -x -c neofetch -l 'yoffset' -d 'Offset in px, top edge'
complete -x -c neofetch -l 'bg_color' -d 'Background color when transparent image'
complete -x -c neofetch -l 'gap' -d 'Gap between image & text'
complete -f -c neofetch -l 'clean' -d 'Delete chached files & thumbnails'

# }}
# Other {{{

complete -r -c neofetch -l 'config' -a 'none\t Run without a config file' -d 'Specify custom config file'
complete -x -c neofetch -l 'print_config' -d 'Print the config file'
complete -f -c neofetch -l 'stdout' -d 'Print without colors & image'
complete -x -c neofetch -l 'help' -d 'Print the help text'
complete -x -c neofetch -l 'version' -d 'Print version'
complete -f -c neofetch -s 'v' -d 'Verbose'
complete -f -c neofetch -s 'vv' -d 'Extra verbose'

# }}}
# Developer {{{

complete -x -c neofetch -l 'gen-man' -d 'Generate man page'

# }}}
