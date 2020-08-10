# Refactored by Jacob Hrbek <kreyren@rixotstudio.cz> in 18.08.2020 20:39:42 CEST

# NOTICE: Shell is written to be POSIX compatible

# Define if blank
PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man
DESTDIR ?= /
SHELL ?= /bin/sh

.PHONY: all clean build list

#@ Default target invoked on 'make' (outputs syntax error on this project)
all:
	@ $(error Target 'all' is not allowed, use 'make list' to list available targets or read the 'Makefile' file)
	@ exit 2

#@ List all targets
list:
	@ true \
		&& grep -A 1 "^#@.*" Makefile | sed s/--//gm | sed s/:.*//gm | sed "s/#@/#/gm" | while IFS= read -r line; do \
			case "$$line" in \
				"#"*|"") printf '%s\n' "$$line" ;; \
				*) printf '%s\n' "make $$line"; \
			esac; \
		done

#@ Install Neofetch in DESTDIR/PREFIX/bin/neofetch and it's man page in DESTRIR/MANDIR/man1
install:
	@ [ -d "$(DESTDIR)$(PREFIX)/bin" ] || mkdir -p "$(DESTDIR)$(PREFIX)/bin"
	@ [ -d "$(DESTDIR)$(MANDIR)/man1" ] || mkdir -p "$(DESTDIR)$(MANDIR)/man1"
	@ [ -f "$(DESTDIR)$(PREFIX)/bin/neofetch" ] || cp -p neofetch "$(DESTDIR)$(PREFIX)/bin/neofetch"
	@ [ -f "$(DESTDIR)$(MANDIR)/man1" ] || cp -p neofetch.1 "$(DESTDIR)$(MANDIR)/man1"
	@ [ -x "$(DESTDIR)$(PREFIX)/bin/neofetch" ] || chmod +x "$(DESTDIR)$(PREFIX)/bin/neofetch"

#@ Uninstall Neofetch
uninstall:
	@ [ -f "$(DESTDIR)$(PREFIX)/bin/neofetch" ] || rm -rf "$(DESTDIR)$(PREFIX)/bin/neofetch"
	@ [ -f "$(DESTDIR)$(MANDIR)/man1/neofetch.1*" ] || rm -rf "$(DESTDIR)$(MANDIR)/man1/neofetch.1*"
