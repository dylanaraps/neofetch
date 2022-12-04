# Maintainer: Sahan Rasanjana <sahan.user@gmail.com>
pkgname=asl-neofetch
_pkgname=asl-neofetch
pkgver=1
pkgrel=1
pkgdesc="A CLI system information tool written in BASH that supports displaying images."
arch=('any')
url="https://github.com/sahanuser/${pkgname}"
license=('MIT')
provides=($_pkgname)
conflicts=($_pkgname 'neofetch' 'neofetch-git')
depends=('bash')
optdepends=(
  'feh: Wallpaper Display'
  'imagemagick: Image cropping / Thumbnail creation / Take a screenshot'
  'nitrogen: Wallpaper Display'
  'w3m: Display Images'
  'catimg: Display Images'
  'jp2a: Display Images'
  'libcaca: Display Images'
  'xdotool: See https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal'
  'xorg-xdpyinfo: Resolution detection (Single Monitor)'
  'xorg-xprop: Desktop Environment and Window Manager'
  'xorg-xrandr: Resolution detection (Multi Monitor + Refresh rates)'
  'xorg-xwininfo: See https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal'
)
makedepends=('git')
source=("$pkgname::git+https://github.com/sahanuser/asl-neofetch.git")
md5sums=('SKIP')

#pkgver() {
#  cd $pkgname
#  git describe --tags --long | sed -r -e 's,^[^0-9]*,,;s,([^-]*-g),r\1,;s,[-_],.,g'
#}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" install
  install -D -m644 LICENSE.md "$pkgdir/usr/share/licenses/neofetch/LICENSE.md"
}
