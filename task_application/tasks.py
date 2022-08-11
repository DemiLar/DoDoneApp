from account.models import CustomizeUser
from task_application.models import Task
from dodone_project.celery import app
from django.core.mail import send_mail
from datetime import timedelta, datetime, date


@app.task
def send_task_with_tomorrow_deadline(user_id):

    user = CustomizeUser.objects.get(id=user_id)
    try:
        task = Task.objects.filter(user_id=user).filter(due_date=datetime.now() + timedelta(days=1))
        subject = f'DoDone Reminder'
        message = f'Good morning, {user.first_name}!\n\nThe task {task.title} has deadline tomorrow.\nHurry up!'
        mail_sent = send_mail(subject,
                              message,
                              'crazydemon713@gmail.com',
                              [user.email])
    except:
        subject = f'DoDone Reminder'
        message = f'Good morning, {user.first_name}!\n\nGood luck with your assignments!'
        mail_sent = send_mail(subject,
                              message,
                              'crazydemon713@gmail.com',
                              [user.email])
    return mail_sent


today = date.today()
last_monday = today - timedelta(days=today.weekday())
one_week = timedelta(days=6)
end_of_week = last_monday + one_week


@app.task
def send_completed_tasks(user_id):

    user = CustomizeUser.objects.get(id=user_id)
    try:
        task = Task.objects.filter(user_id=user).filter(status='finished').\
            filter(done_date=last_monday + one_week)
        subject = f'DoDone Reminder'
        message = f'Good morning, {user.first_name}!\n\nCompleted tasks this week: {task.title}\n\nGood job!'
        mail_sent = send_mail(subject,
                              message,
                              'crazydemon713@gmail.com',
                              [user.email])
    except:
        subject = f'DoDone Reminder'
        message = f'Good morning, {user.first_name}!\n\nYou don’t have completed tasks ((\n\nTry harder!'
        mail_sent = send_mail(subject,
                              message,
                              'crazydemon713@gmail.com',
                              [user.email])
    return mail_sent