from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQCseIaZHiBMajz6p21kdxKNjbHeZcgwKUb-jLHEjz8KEpsaKfQzn1PKCMyNss4bV615YXWlz2Mp7P__Np1NE360mpnVfn3hz1Snks55Sga1IRuupZRSN2D6UPeSsUtBH-4f8eXGAHSo5M_oMYx42GzCMBZ-xqNVEXxM1glZK4kfM5Oq02x9mX1g6rhA9RT3lZjMoIvKDixifQV_PgoWJY1KBNOHBKaQZJ1axIjCfRHUZk5vj9BrV1wMRp_7LX3SE5CUtw-le8O253JlIvqOs79BboSTAdnEcOIasWWlfmY-Q_IzhRzdw5MpNGkxa2l8Yb7JqqAlDihMadIUXr4fFXMLAAAAAVMMSsYA")

BOT_TOKEN = getenv("BOT_TOKEN", "5656196788:AAFh_GWyY8FO2zxhQ8IrgO_ST1TyMR-lSVM")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BlackWorldMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheBothub")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6190680150").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6190680150").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
