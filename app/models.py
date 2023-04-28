from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class Follows(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    #__tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def __init__(self, follower_id, user_id):
        self.follower_id = follower_id
        self.user_id = user_id
        self.created_on = created_on


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Follows %r>' % (self.follower_id)