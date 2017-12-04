from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf import Form


class CourseForm(Form):
    courseId = StringField('Course Id', validators=[DataRequired()])
    courseName = StringField('Course Name', validators=[DataRequired()])
    courseDesc = StringField('Course Description', validators=[DataRequired()])

class TopicsForm(Form):
    topicname = StringField('Topic', validators=[DataRequired()])
    topicdisc = StringField('Discussion', validators=[DataRequired()])
    courseid = StringField('Course Id', validators=[DataRequired()])