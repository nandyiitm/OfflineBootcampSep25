from celery import Celery

# initialize Celery application
celeryApp = Celery(
    'tasks',
    broker='redis://localhost:6379/0'
)

# Optional: Configure Celery settings
celeryApp.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

# tasks

from mail import send_email
from app import app
from models import User

@celeryApp.task()
def daily_reminder():

    with app.app_context():
        for user in User.query.all():
            to = user.email
            subject = "Daily Reminder"
            body = f"Hello {user.name}, this is your daily reminder to visit out application."
            send_email(to, subject, body)
    return "Daily reminders sent!"

@celeryApp.task()
def monthly_newsletter():

    with app.app_context():
        for user in User.query.all():
            to = user.email
            subject = "Monthly Newsletter"
            body = f"Hello {user.name}, welcome to our monthly newsletter!"
            send_email(to, subject, body)
    return "Monthly newsletters sent!"

@celeryApp.task()
def export_csv():
    # Placeholder for CSV export logic
    # This function would contain the logic to export data to a CSV file
    return "CSV export completed!"


# schedule tasks


