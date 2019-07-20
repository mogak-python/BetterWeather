from slacker import Slacker

from config import BOT_USER_OAUTH_ACCESS_TOKEN

slack = Slacker(BOT_USER_OAUTH_ACCESS_TOKEN)
slack.chat.post_message('#bots_test', '날씨알리미')
