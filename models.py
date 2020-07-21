from flask_sqlalchemy import SQLAlchemy
DB = SQLAlchemy()




TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                 'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                 'common_squirrel', 'KenJennings', 'conanobrien',
                 'big_ben_clock', 'IAM_SHAKESPEARE']

class User(DB.Model):
    """ Twitter users."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return 'User {}'.format(self.name)
    
class Tweet(DB.Model):
    ## Tweets and the embeddings
    id = DB.Column(DB.BigIntger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationsip('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '[Tweet {}]'.format(self.text)
        
    
    
def add_test_users():
    for i, name in enumerate(TWITTER_USERS):
        user = User(id=i, name=name)
        DB.session.add(user)
    DB.session.commit()