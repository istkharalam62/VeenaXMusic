from VeenaXMusic.core.bot import Veena
from VeenaXMusic.core.dir import dirr
from VeenaXMusic.core.git import git
from VeenaXMusic.core.userbot import Userbot
from VeenaXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Veena()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
