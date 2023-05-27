from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(35), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    playlist_songs = db.relationship('PlaylistSong', backref='playlist', cascade="all, delete-orphan")



class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    artist = db.Column(db.String(16), nullable=False, unique=True)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id', ondelete='CASCADE'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
    song = db.relationship('Song', backref='playlist_songs')

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to the database."""

    db.app = app
    db.init_app(app)
