from db import db
from datetime import datetime, timezone


# Define Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    project = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    aipl_job_reference = db.Column(db.String(50), nullable=False)
    customer_representative = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    pre_order_service = db.Column(db.Integer, nullable=False)
    post_order_handling = db.Column(db.Integer, nullable=False)
    on_time_delivery = db.Column(db.Integer, nullable=False)
    quality_sustenance = db.Column(db.Integer, nullable=False)
    overall_response = db.Column(db.Integer, nullable=False)
    final_documentation = db.Column(db.Integer, nullable=False)
    appraisal = db.Column(db.Integer, nullable=False)
    compliance = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500))
    timestamp = db.Column(db.String(100), nullable=False)

    # Method to calculate the average of all radio button values
    def average_rating(self):
        total = (self.pre_order_service + self.post_order_handling +
                 self.on_time_delivery + self.quality_sustenance +
                 self.overall_response + self.final_documentation +
                 self.appraisal + self.compliance)
        return total / 8  # Since there are 8 radio fields
