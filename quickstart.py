from instapy import InstaPy

insta_username = 'smm_teamdroidx'
insta_password = 'hksj@BC69'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password, nogui=True)
session.login()

# do the actual liking
session.like_by_tags(['entrepreneur', 'grind', 'motivation', 'automation', 'business', 'success', 'teamdroidx'], amount=25)

# default enabled=False, follows ~ 10% of the users from the images, times=1
# (only follows a user once (if unfollowed again))
session.set_do_follow(enabled=True, percentage=10, times=1)

# Follows the followers of each given user
# The usernames can be either a list or a string
# The amount is for each account, in this case 30 users will be followed
# If randomize is false it will pick in a top-down fashion
# default sleep_delay=600 (10min) for every 10 user following, in this case
# sleep for 60 seconds
session.follow_user_followers(['evandantas', 'secret2success', 'garyvee'], amount=10, randomize=False, sleep_delay=60)

# end the bot session
session.end()
