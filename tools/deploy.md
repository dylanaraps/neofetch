### Things to do before deploying...

* [x] Check file permissions (+x)
* [x] Check Shellcheck (should be automatic)
* [x] Update version numbers (`README.md`, `package.json`, `hyfetch/constants.py`, `neofetch`)
* [x] Update distro list in neofetch help (`tools/list_distros.py`)
* [x] Regenerate man page (`help2man ./neofetch > neofetch.1`)
* [ ] Create an RC release and deploy to pypi, try installing and testing on many distros.
* [ ] Change back to stable release, create tag, create GitHub release
* [x] Formally deploy to pypi and npm (`tools/deploy.sh`, `npm publish`)
* [ ] Update ArchLinux AUR and NixOS packaging
