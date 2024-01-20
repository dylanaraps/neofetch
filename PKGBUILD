pkgname=neofetch
pkgver=7.1.0
pkgrel=3
pkgdesc='Neofetch for aerOS'
arch=('any')
url='https://github.com/hewol/aeros-neofetch'
license=('MIT')
depends=('bash')
makedepends=('p7zip' 'wget')
backup=('etc/neofetch/config.conf')
optdepends=(
  'catimg: Display Images'
  'chafa: Image to text support'
  'feh: Wallpaper Display'
  'imagemagick: Image cropping / Thumbnail creation / Take a screenshot'
  'jp2a: Display Images'
  'libcaca: Display Images'
  'nitrogen: Wallpaper Display'
  'w3m: Display Images'
  'xdotool: See https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal'
  'xorg-xdpyinfo: Resolution detection (Single Monitor)'
  'xorg-xprop: Desktop Environment and Window Manager'
  'xorg-xrandr: Resolution detection (Multi Monitor + Refresh rates)'
  'xorg-xwininfo: See https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal'
)
source=('https://github.com/hewol/aeros-neofetch/archive/refs/heads/master.zip')
sha256sums=('SKIP')

package() {
  mkdir ./$pkgname
  cd ./$pkgname
  wget $source
  7z e -o. *.zip
  rm *.zip
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}
