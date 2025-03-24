import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = 25695415
API_HASH = "38a4b64f718fbe909cb54d083a7d1d46"
# ------------------------------------------------------
BOT_TOKEN = "7816530829:AAH9bMux2HEgfryvbOBPX09KTfAofmH1ikg"
# -------------------------------------------------------
OWNER_USERNAME = "bokuwa_aizen"
# --------------------------------------------------------
BOT_USERNAME = "boamsicxbot"
# --------------------------------------------------------
BOT_NAME = "˹𝐁ᴏᴀ ꭙ 𝐌ᴜsɪᴄ˼"
# ---------------------------------------------------------
ASSUSERNAME = "boa_x_assistant"
# ---------------------------------------------------------
SERVER_PLAYLIST_LIMIT = "100"


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = "mongodb+srv://aizencookies7:boa3@cluster0.udbnj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#---------------------------------------------------------------

#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------
ADDLISTLOG_ID = -1002273184049
# ----------------------------------------------------------------
LOGGER_ID = -1002070231017
# ----------------------------------------------------------------
REMOVELISTLOG_ID = -1002204817043
# ----------------------------------------------------------------
OWNER_ID = 6806897901
# ----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Lord-Devine/advance",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "githuBA0J19itA9L76Qn_FwWd8WrN0o3vBWqhGppNw2evTLpzDa3JZ0zUzswsUdR3GZHLE3If8erTyHx"
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = "https://t.me/soul_x_network"
SUPPORT_CHAT = "https://t.me/soul_x_society"
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = "1c21247d714244ddbb09925dac565aed"
SPOTIFY_CLIENT_SECRET = "709e1a2969664491b58200860623ef19"
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = "BQFr_7YAYwqdjkg50VKqTLI1d8uPK_9jQiHd2KzWL5vEKbGCR51_5WBw-WKGnXDdm5Squ5RWJ9YAVpiFyFxseY0Vh2RKgW0LWoUlvHM5MRZuo9fEMIc-P2l0w5MzMvWvn0rvrqyERFZU14x-B_-WBYk2twbzF9hjWis9w3dUS3yfiMwtTCXgaCHk0ztjA2X_hlGWacIYiAcB8L8ePHlOSd-mW-d8Z1geSBF7ILoyruljtJfkBt6dGJ8020ZSqFotA9-gQUoWyhuR-ldAC7ODKt6x-y1De0_81-WSr4JSDU6I_UHbHkenUgwp2q4jYmIJmdjqaDcOrmI4T47fCW7aHJNMeTazZQAAAAG0iTNMAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

filter = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/zv3jss.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/zv3jss.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
STATS_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/5dl0e2.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/5dl0e2.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/5dl0e2.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
