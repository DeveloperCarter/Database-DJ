"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relation, relationship

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    playlistsong = relationship('PlaylistSong', backref='playlist')


class Song(db.Model):
    """Song."""
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    playlistsong = relationship('PlaylistSong', backref='song')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlistsong'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
