### Things to do before deploying...

* [ ] Check file permissions (+x)
* [ ] Update version numbers (`README.md`, `package.json`, `hyfetch/constants.py`, `neofetch`)
* [ ] Check Shellcheck (should be automatic)
* [ ] Update distro list in neofetch help (`tools/list_distros.py`)
* [ ] Regenerate man page (`help2man ./neofetch > neofetch.1`)
* [ ] Create an RC release and deploy to pypi, try installing and testing on many distros.
* [ ] Change back to stable release, create tag, create GitHub release
* [ ] Formally deploy to pypi and npm (`tools/deploy.sh`, `npm publish`)
* [ ] Update ArchLinux AUR and NixOS packaging
