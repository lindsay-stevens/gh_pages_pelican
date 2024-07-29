from datetime import date

AUTHOR = "Lindsay Stevens"
SITENAME = "Lindsay Stevens"
SITEURL = "http://localhost:8000"
SITESUBTITLE = "Lindsay Stevens"
SITELOGO = SITEURL + "/img/profile.png"

PATH = "content"

TIMEZONE = "Australia/Sydney"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    #("blog", "/blog_index.html"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/lindsay-stevens"),
    ("linkedin", "https://www.linkedin.com/in/lindsay-stevens-83b17875"),
)

DEFAULT_PAGINATION = False
STATIC_PATHS = ["css", "extra", "icons", "img"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}
CUSTOM_CSS = "/css/styles.css"
INDEX_SAVE_AS = "blog_index.html"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Flex options
# Theme: https://github.com/alexandrevicenzi/Flex
THEME = "themes/flex_2.5.0"
USE_GOOGLE_FONTS = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
COPYRIGHT_YEAR = date.today().year
DISABLE_URL_HASH = True
