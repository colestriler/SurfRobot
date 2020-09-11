import tweepy
from flaskapp.bots.config_class import API


api_class = API()
api = api_class.create_api()


pro_surfers = ['bethanyhamilton', 'kellyslater',
             'jordysmith88', #san clemente
             "surfer", "Kai_Lenny", "CaioIbelli", 'nikkivandijk_', '_VicVergara',
             'KSWaveCo', 'cbasszietz']



def follow():
    # num_followed = 0
    # while num_followed <= 15:
    #     for follower in api.followers('bethanyhamilton', count=5):
    #         if follower.location == "Carlsbad, CA":
    #             api.create_friendship(id = follower.id)
    #             num_followed+=1

    num_followed = 0
    while num_followed < 30:
        for tweet in tweepy.Cursor(api.search, q="#surfing").items():
            # api.create_friendship(tweet.author.screen_name)
            print(tweet.author.screen_name)
            num_followed += 1
        # api.create_friendship(id = follower.id)


# limit = api.rate_limit_status()
# limit['resources']['followers']['/followers/ids']['remaining']
#
# limit['resources']['followers']['/followers/list']['remaining']
#
# limit['resources']['friendships']


# api.show_friendship(source_id=surfrobot.id, target_id=cole.id)
# (Friendship(_api=<tweepy.api.API object at 0x10cfd0358>, _json={
# 'id': 1184003500247642114,
# 'id_str': '1184003500247642114',
# 'screen_name': 'SurfRobot',
# 'following': True,
# 'followed_by': True,
# 'live_following': False,
# 'following_received': None,
# 'following_requested': None,
# 'notifications_enabled': None,
# 'can_dm': True, 'blocking': None,
# 'blocked_by': None,
# 'muting': None,
# 'want_retweets': None,
# 'all_replies': None,
# 'marked_spam': None},
# id=1184003500247642114, id_str='1184003500247642114', screen_name='SurfRobot', following=True, followed_by=True, live_following=False, following_received=None, following_requested=None, notifications_enabled=None, can_dm=True, blocking=None, blocked_by=None, muting=None, want_retweets=None, all_replies=None, marked_spam=None), Friendship(_api=<tweepy.api.API object at 0x10cfd0358>, _json={'id': 2594449783, 'id_str': '2594449783', 'screen_name': 'ColeStriler', 'following': True, 'followed_by': True, 'following_received': None, 'following_requested': None}, id=2594449783, id_str='2594449783', screen_name='ColeStriler', following=True, followed_by=True, following_received=None, following_requested=None))



# surfrobot = api.get_user('surfrobot')
# cole = api.get_user('cole')
# friendship = api.show_friendship(source_id=surfrobot.id, target_id=cole.id)
