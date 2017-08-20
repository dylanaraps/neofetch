PREFIX ?= /usr
SYSCONFDIR ?= /etc
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'make install\' to install Neofetch.

install:
	@echo 'Making directories...'
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(PREFIX)/share/neofetch/ascii/distro
	@mkdir -p $(DESTDIR)$(MANDIR)/man1
	@mkdir -p $(DESTDIR)$(SYSCONFDIR)/neofetch

	@echo 'Installing binaries...'
	@sed "s|ASCIIDIR|$(PREFIX)/share/neofetch/ascii/distro|g;s|CONFDIR|$(SYSCONFDIR)/neofetch|g" < neofetch > $(DESTDIR)$(PREFIX)/bin/neofetch
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/neofetch

	@echo 'Installing ASCII files, man page and config file...'
	@cp -p ascii/distro/* $(DESTDIR)$(PREFIX)/share/neofetch/ascii/distro
	@cp -p neofetch.1 $(DESTDIR)$(MANDIR)/man1
	@cp -p config/config.conf $(DESTDIR)$(SYSCONFDIR)/neofetch/config.conf

uninstall:
	@echo 'Removing files...'
	@rm -rf $(DESTDIR)$(PREFIX)/bin/neofetch
	@rm -rf $(DESTDIR)$(MANDIR)/man1/neofetch.1*
	@rm -rf $(DESTDIR)$(PREFIX)/share/neofetch
	@rm -rf $(DESTDIR)$(SYSCONFDIR)/neofetch
