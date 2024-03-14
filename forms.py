from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length
from wtforms import SubmitField


class UploadForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    file = FileField(
        FileRequired('File Should Not be Empty')
    )
    submit = SubmitField('Upload')
