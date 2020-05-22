# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import os,gettext

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os.environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("WeatherPlugin2", resolveFilename(SCOPE_PLUGINS, "Extensions/WeatherPlugin2/locale"))

def _(txt):
	t = gettext.dgettext("WeatherPlugin2", txt)
	if t == txt:
		print "[WeatherPlugin2] fallback to default translation for", txt
		t = gettext.gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)
