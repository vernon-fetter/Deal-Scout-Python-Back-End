import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

APP_NAME = "Deal-n-All"

FAB_SECURITY_MANAGER_CLASS='app.security.MySecurityManager'

# Uncomment to setup Setup an App icon
# APP_ICON = "static/img/logo.jpg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# OAUTH_PROVIDERS = [
#     {'name':'facebook', 'icon':'fa-facebook',
#         'remote_app': {
#             'consumer_key':'FACEBOOK_APP_ID',
#             'consumer_secret':'FACEBOOK_APP_SECRET',
#             'base_url':'https://graph.facebook.com/',
#             'request_token_params':{
#               'scope': 'email'
#             },
#             'request_token_url':None,
#             'access_token_url':'/oauth/access_token',
#             'authorize_url':'https://www.facebook.com/dialog/oauth'}
#     },
#     {'name':'google', 'icon':'fa-google', 'token_key':'access_token',
#         'remote_app': {
#             'consumer_key':'976274410989-1hassd93t8g7dj6bbs1u9qk4cd085nad.apps.googleusercontent.com',
#             'consumer_secret':'AuSHli4TGTdbqhHBIJa1dHQZ',
#             'base_url':'https://www.googleapis.com/oauth2/v2/',
#             'request_token_params':{
#               'scope': 'email profile'
#             },
#             'request_token_url':None,
#             'access_token_url':'https://accounts.google.com/o/oauth2/token',
#             'authorize_url':'https://accounts.google.com/o/oauth2/auth'}
#     }
# ]

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Administrator'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'User'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = 'User'

RECAPTCHA_PUBLIC_KEY = "6Ldh0sUUAAAAAM6TsvjL3j-bYAUbXcQt-Ev4j7mM"
RECAPTCHA_PRIVATE_KEY = "6Ldh0sUUAAAAAK3xWc0u_vwqO2K-BMYi-cHMDh2z"

MAIL_PORT = 993
MAIL_SERVER = 'mail.gandi.net'
MAIL_USE_SSL = True
MAIL_USE_TLS = True
MAIL_USERNAME = 'vernon.fetter@cyberflex.io'
MAIL_PASSWORD = 'VernonKoek123*'
MAIL_DEFAULT_SENDER = 'vernon.fetter@cyberflex.io'

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    # "pt": {"flag": "pt", "name": "Portuguese"},
    # "pt_BR": {"flag": "br", "name": "Pt Brazil"},
    # "es": {"flag": "es", "name": "Spanish"},
    # "de": {"flag": "de", "name": "German"},
    # "zh": {"flag": "cn", "name": "Chinese"},
    # "ru": {"flag": "ru", "name": "Russian"},
    # "pl": {"flag": "pl", "name": "Polish"},
}
# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
TEMP_FOLDER = basedir + '/app/static/uploads/'
# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
APP_THEME = "slate.css"
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"

FAB_API_SWAGGER_UI = True
