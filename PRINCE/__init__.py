from PRINCE.core.bot import Sona
from PRINCE.core.dir import dirr
from PRINCE.core.git import git
from PRINCE.core.userbot import Userbot
from PRINCE.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sona()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
