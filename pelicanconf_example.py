# -*- coding: utf-8 -*- #
# Pelican configuration file

# --- Imports ---
from datetime import datetime
import os
import locale
from pelican import signals


# --- Set Locale ---
def set_locale():
    try:
        locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
    except locale.Error:
        print("Yerel ayar desteklenmiyor. Varsayılan yerel ayarlar kullanılacak.")


set_locale()

# --- Environmental Variables ---
PUBLISH = os.environ.get("PUBLISH")

# --- Basic Settings ---
TIMEZONE = "Europe/Istanbul"
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"
DATE_FORMATS = {
    "en": "%B %d, %Y",
}
AUTHOR = "yuceltoluyag"
SITENAME = "Babanın Yeni Evi"
DESCRIPTION = "Your site description here"
SITESUBTITLE = "yARRAQ GiBi Hay4T"
KEYWORDS = "your, keywords, here"
SITEURL = "https://yuceltoluyag.github.io" if PUBLISH else "http://localhost:8000"
CANONICAL_URL = SITEURL
DELETE_OUTPUT_DIRECTORY = True
DISABLE_URL_HASH = True
BROWSER_COLOR = "#333333"
# PYGMENTS_STYLE = "monokai"
ROBOTS = "index, follow"

# Yıl değişkeni
SITEYEAR = datetime.now().year
# Version değişkeni
VERSION = "1.0.0"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
USE_LESS = True

# --- Paths & Directories ---
THEME_STATIC_DIR = "assets"
THEME = "themes/Baba2"
IMAGE = "path/to/your/image.png"
AVATAR = "https://jaze.top/avatar.png"

PATH = "content"
STATIC_PATHS = [
    "images",
    "extra",
]
EXTRA_PATH_METADATA = {
    "extra/SW.js": {"path": "SW.js"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon.webp": {"path": "favicon.webp"},
}

# --- Table of Content Plugin ---
TOC = {
    "TOC_HEADERS": "^h[1-3]",
    "TOC_RUN": "true",
    "TOC_INCLUDE_TITLE": "false",
}

# --- Social Media ---
SOCIAL = {
    "mastodon": "yuceltoluyag",
    "matrix": "friday13",
    "discord": "188034964879573003",
    "github": "yuceltoluyag",
    "instagram": "yuceltoluyag",
    "youtube": "@yuceltoluyag",
    "twitch": "yuceltoluyag",
    "buymeacoffee": "friday13",
    "github_sponsor": "yuceltoluyag",
}

# --- Menu Items ---
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

NAVBAR_LINKS = [
    {"name": "Home", "url": "/", "target": "_self"},
    {"name": "About", "url": "/about/", "target": "_self"},
    {"name": "Contact", "url": "/contact/", "target": "_self"},
]

# --- License ---
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

# --- Feed Settings ---
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
HOME_HIDE_TAGS = True
# USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

# --- Pagination Settings ---
DEFAULT_PAGINATION = 6
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)
PAGINATED_TEMPLATES = {"index": None, "tag": None, "category": None, "author": None}

WIDGETS = [
    "category.html",
    "recent_posts.html",
    "search.html",
    "tag.html",
    "tagcloud.html",
]
# --- Markdown Extensions ---
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.toc": {"title": "Table of Contents", "toc_depth": 3},
    },
    "output_format": "html5",
}

# --- Plugin Settings ---
PLUGIN_PATHS = ["plugins"]

common_plugins = [
    "plugins.pelican-toc",
    "pelican.plugins.sitemap",
    "pelican.plugins.related_posts",
    "plugins.fix_sitemap",
    "pelican.plugins.neighbors",
    "pelican.plugins.seo",
    "minchin.pelican.plugins.post_stats",
    "pelican.plugins.series",
]

dev_plugins = common_plugins.copy()

prod_extra_plugins = [
    "plugins.search",
    "plugins.minify",
]

prod_plugins = common_plugins + prod_extra_plugins

PLUGINS = prod_plugins if PUBLISH else dev_plugins

# --- SEO Settings ---
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = False  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False  # Subfeature of SEO enhancer
SEO_ARTICLES_LIMIT = 10
SEO_PAGES_LIMIT = 10

# --- Google Analytics ---
GTAG = "G-9VKX48YDBH" if PUBLISH else None

# --- Google Affiliate Settings ---
