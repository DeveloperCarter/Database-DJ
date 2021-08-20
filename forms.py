"""Forms for playlist app."""

from typing import Text
from wtforms.validators import InputRequired, Optional
from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.widgets.core import Input


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[Optional()])

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    song_name = StringField('Song Name', validators=[InputRequired()])
    artist_name = StringField('Artist Name', validators=[InputRequired()])
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
