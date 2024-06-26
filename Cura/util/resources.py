"""
Helper module to get easy access to the path where resources are stored.
This is because the resource location is depended on the packaging method and OS
"""
__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import os
import sys
import glob
import gettext

if sys.platform.startswith('darwin'):
	try:
		#Foundation import can crash on some MacOS installs
		from Foundation import *
	except:
		pass

if sys.platform.startswith('darwin'):
	if hasattr(sys, 'frozen'):
		try:
			resourceBasePath = NSBundle.mainBundle().resourcePath()
		except:
			resourceBasePath = os.path.join(os.path.dirname(__file__), "../../../../../resources")
	else:
		resourceBasePath = os.path.join(os.path.dirname(__file__), "../../resources")
else:
	resourceBasePath = os.path.join(os.path.dirname(__file__), "../../resources")

def getPathForResource(dir, subdir, resource_name):
	assert os.path.isdir(dir), "{p} is not a directory".format(p=dir)
	path = os.path.normpath(os.path.join(dir, subdir, resource_name))
	assert os.path.isfile(path), "{p} is not a file.".format(p=path)
	return path

def getPathForImage(name):
	return getPathForResource(resourceBasePath, 'images', name)

def getPathForMesh(name):
	return getPathForResource(resourceBasePath, 'meshes', name)

def getPathForFirmware(name):
	return getPathForResource(resourceBasePath, 'firmware', name)

def getPathForXML(name):
	return getPathForResource(resourceBasePath, 'xml', name)

def setupLocalization(selectedLanguage = None):
	#Default to english
	languages = ['en']

	if selectedLanguage is not None:
		for item in getLanguageOptions():
			if item[1] == selectedLanguage and item[0] is not None:
				languages = [item[0]]

	locale_path = os.path.normpath(os.path.join(resourceBasePath, 'locale'))
	translation = gettext.translation('Cura', locale_path, languages, fallback=True)
	translation.install()

def getLanguageOptions():
	return [
		['en', 'English'],
		['fr', 'French']
	]

def getPrinters():
	printers = []
	printers_file = open(os.path.normpath(os.path.join(resourceBasePath, 'printers', 'list.txt')), 'r')
	for line in printers_file:
		if not line.startswith('#'):
			sline = line.split(';')
			name = sline[0].rstrip()
			desc = ''
			if len(sline) > 1:
				desc = sline[1].rstrip()
			config = name.lower() + '.xml'
			img = name.lower() + '.png'
			if not os.path.isfile(os.path.join(resourceBasePath, 'images', img)):
				img = 'default.png'
			if os.path.isfile(os.path.join(resourceBasePath, 'xml', config)):
				printer = { 'name': name, 'desc': desc, 'config': config, 'img': img }
				printers.append(printer)
	return printers
