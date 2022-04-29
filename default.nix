with import <nixpkgs> {};

callPackage ./nixos/hyfetch.nix {
    buildPythonPackage = python38Packages.buildPythonPackage;
    fetchPypi = python38.pkgs.fetchPypi;
    typing-extensions = python38.pkgs.typing-extensions;
    setuptools = python38.pkgs.setuptools;
}
