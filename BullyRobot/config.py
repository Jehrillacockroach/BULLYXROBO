import json
import os


def get_user_list(config, key):
    with open("{}/BullyRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "9267473"
    API_HASH = "5df447fd1d0daded66056e6921eda448"
    TOKEN = "5185426104:AAFvUQ7XdNx184Ux-XrlItQtZ1KWFE6WgRA"
    OWNER_ID = "2078119261"
    OWNER_USERNAME = "jehrilla_cockroach"
    SUPPORT_CHAT = "BullyxSupprt"
    JOIN_LOGGER = (-1001738311599)
    EVENT_LOGS = (-1001738311599)

    SQLALCHEMY_DATABASE_URI = "postgres://tgvgozsn:FDWXT8tkjerwETvcfxDENH5aAdwFASod@isilo.db.elephantsql.com/tgvgozsn"
    MONGO_DB_URI = "mongodb+srv://FreeFire:rihan56756756@cluster0.8wcg2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/jehrilla_cockroach"
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = "D0ZCZ67KL8OTL0PY"
    TIME_API_KEY = "5LB4TAKPEKZ0"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
