# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError

class FeedbackForm(FlaskForm):
    # Text Fields
    customer_name = StringField('Customer Name', validators=[DataRequired(), Length(min=2, max=100)])
    project = StringField('Project', validators=[DataRequired(), Length(min=2, max=100)])
    product = StringField('Product', validators=[DataRequired(), Length(min=2, max=100)])
    aipl_job_reference = StringField('AIPL Job Reference (Ex. J 2121)', validators=[DataRequired(), Length(min=6, max=6), Regexp(r'^J\s\d{4}$', message="AIPL Job Reference must be in the format 'J ####' (e.g., J 2121)")])
    customer_representative = StringField('Customer Representative', validators=[DataRequired(), Length(min=2, max=100)])
    designation = StringField('Designation', validators=[DataRequired(), Length(min=2, max=100)])
    
    # Radio Button Fields with values from 5 (Excellent) to 1 (Poor)
    pre_order_service = RadioField('Pre-Order Service', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    post_order_handling = RadioField('Post Order Handling', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    on_time_delivery = RadioField('On Time Delivery', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    quality_sustenance = RadioField('Quality Sustenance', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    overall_response = RadioField('Overall Response', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    final_documentation = RadioField('Final Documentation', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    appraisal = RadioField('Appraisal for Further Enquiries/Orders', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    compliance = RadioField('Compliance to Engineering Standards', choices=[(5, 'Excellent'), (4, 'Better'), (3, 'Good'), (2, 'Average'), (1, 'Poor')], coerce=int, validators=[DataRequired()])
    
    # Text Area Field for Comments
    comments = TextAreaField('Any Comments', validators=[DataRequired(), Length(max=500)])
    
    # Submit Button
    submit = SubmitField('Submit Feedback')

class LoginForm(FlaskForm):
    # Username and Password Fields for Admin Login
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=100)])
    
    # Submit Button
    submit = SubmitField('Login')
