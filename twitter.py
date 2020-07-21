""" Retreive tweets, embeddings and persist in the database"""
import tweepy
import basilica
from .models import DB, Tweet, User

TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                 'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                 'common_squirrel', 'KenJennings', 'conanobrien',
                 'big_ben_clock', 'IAM_SHAKESPEARE']

TWITTER_AUTH = tweepy.OAuthHandler(
    '1270091384528285698-doa2xsVdxD2a6sz5n672bhIK2Nc6u0'
    'ipQFTt2O9d0F9uAuJvawi4jcw9pZyP9m7DZGv0c04TSwr' 
)

TWITTER = tweepy.API(TWITTER_AUTH)

def add_or_update(username):
    """ ADD or update a user and their Tweets, error if not a twitter user."""
    try:
        twitter_user = TWITTER.get_user(username)
        db_user = (User.query.get(twiiter_user.id) or
                   User(id=twitter_user.id, name=username))
        DB.session.add(db_user)
        tweets = twitter_user.timeline(
            count=200, exclude_repllies=True, include_rts=False,
            tweet_mode = 'extended', since_id=user.newest_tweet_id)
        )
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        for tweet in tweets:
            db_tweet = Tweet(id=tweet.id, text = tweet.full_text[:300])
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
        except Exception as e:
            print('Error Processing {}: {}'.format(username, e))
            raise e
        else:
            DB.session.commit()
def add_users(users=TWITTER_USERS):
    """ ADD a list or tuple """
    pass