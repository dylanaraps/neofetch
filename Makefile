SHELL = /bin/sh
PROGRAM = neofetch

PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man



all:
	@ printf "%s\n" "Run 'make install' as superuser to install Neofetch on this system."

install:
	@ mkdir -p $(DESTDIR)$(PREFIX)/bin
	@ mkdir -p $(DESTDIR)$(MANDIR)/man1
	@ cp -p neofetch $(DESTDIR)$(PREFIX)/bin/neofetch
	@ cp -p neofetch.1 $(DESTDIR)$(MANDIR)/man1
	@ chmod 755 $(DESTDIR)$(PREFIX)/bin/neofetch
	@ if command -v ${PROGRAM} >/dev/null; then printf "%s\n" "${PROGRAM} has been installed on this system."; fi
	@ if ! command -v ${PROGRAM} >/dev/null; then printf "%s\n" "Failed to install ${PROGRAM} on this system."; fi
	

uninstall:
	@ rm -rf $(DESTDIR)$(PREFIX)/bin/neofetch
	@ rm -rf $(DESTDIR)$(MANDIR)/man1/neofetch.1*
	@ if ! command -v ${PROGRAM} >/dev/null; then printf "%s\n" "${PROGRAM} has been removed from this system."; fi
	@ if command -v ${PROGRAM} >/dev/null; then printf "%s\n" "Failed to remove ${PROGRAM} from system."; fi
