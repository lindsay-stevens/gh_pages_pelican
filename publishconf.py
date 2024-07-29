# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

from datetime import date
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.lindsay-stevens.com.au'
SITELOGO = SITEURL + '/img/profile.png'
RELATIVE_URLS = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True

COPYRIGHT_YEAR = date.today().year

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
