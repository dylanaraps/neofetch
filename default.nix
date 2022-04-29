with import <nixpkgs> {};

callPackage ./nixos/hyfetch.nix {
    python3Packages = python38Packages;
}
