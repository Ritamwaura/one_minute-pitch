from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required 

class ReviewForm(FlaskForm):
    title = StringField('Comment')
    comment = TextAreaField('Enter your comment')
    submit = SubmitField('submit')
    
    class UpdateProfile(FlaskForm):
        bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')