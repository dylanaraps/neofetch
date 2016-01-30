PREFIX        ?=  usr
RM            ?=  rm -f
INSTALL_DIR   ?=  install -m755 -d
INSTALL_PROG  ?=  install -m755 -D
INSTALL_FILE  ?=  install -m644 -D

all:
	@echo Run \'make install\' to install Fetch

install:
	$(INSTALL_DIR) $(DESTDIR)/$(PREFIX)/bin
	$(INSTALL_DIR) $(DESTDIR)/usr/share/fetch/ascii/distro
	$(INSTALL_PROG) fetch $(DESTDIR)/$(PREFIX)/bin/fetch
	$(INSTALL_PROG) config $(DESTDIR)/usr/share/fetch/config
	$(INSTALL_PROG) ascii/distro/* $(DESTDIR)/usr/share/fetch/ascii/distro

uninstall:
	$(RM) $(DESTDIR)/$(PREFIX)/bin/fetch
	$(RM) -r $(DESTDIR)/usr/share/fetch


