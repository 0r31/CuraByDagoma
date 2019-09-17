"""
Helper module to check sha256 sum.
"""
__copyright__ = "Copyright (C) 2019 Dagoma - Released under terms of the AGPLv3 License"

import os
import urllib2

url_handle = None
version_url = "https://dist.dagoma.fr/version/CuraByDagoma"

try:
	url_handle = urllib2.urlopen(version_url)
except urllib2.URLError:
	try:
		import ssl
		context = ssl._create_unverified_context()
		url_handle = urllib2.urlopen(version_url, context=context)
	except:
		pass
except:
	pass

def isLatest():
	if url_handle is None:
		return True
	official_version = url_handle.read()
	return official_version == os.environ['CURABYDAGO_RELEASE_VERSION'] or not isinstance(os.environ['CURABYDAGO_RELEASE_VERSION'].split('.')[-1], int)
