from flask_sqlalchemy import SQLAlchemy

# TODO: connect to a local postgresql database
db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(320))
    seeking_talent = db.Column(db.String())
    seeking_description = db.Column(db.String())
    show = db.relationship('Show', backref=db.backref('venue', lazy='joined'), lazy='joined')

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(320))
    seeking_venue = db.Column(db.String())
    seeking_description = db.Column(db.String())
    show = db.relationship('Show', backref=db.backref('artist', lazy='joined'), lazy='joined')
            
class Show(db.Model):
  __tablename__ = 'Show'
  id = db.Column(db.Integer(), primary_key=True)
  artist_id = db.Column(db.Integer(), db.ForeignKey('Artist.id'), nullable=False)
  venue_id = db.Column(db.Integer(), db.ForeignKey('Venue.id'), nullable=False)
  start_time = db.Column(db.DateTime())