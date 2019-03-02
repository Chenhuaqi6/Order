SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME = 'mooc_food'

##过滤url
IGNORE_URLS=[
    "^/user/login"

]

INNORE_CHECK_LOGIN_URLS = [

    "^/static",
    "^/favicon.ico"

]

API_IGNORE_URLS=[
    "^/api"
]

PAGE_SIZE = 50

PAGE_DISPLAY = 10

STATUS_MAPPING = {
    '1':'正常',
    '0':'已删除'

}

MINA_APP = {
    'appid':'wx0abdbfdf2d171832',
    'appkey':'83078db89c5a506751be03725086a0ce'

}

UPLOAD = {
    'ext':['jpg','gif','jepg','png'],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/',
}

APP = {
    'domain':'http://192.168.43.128:8999',

}