from account.models import CustomizeUser
from dodone_project.celery import app
from django.core.mail import send_mail


@app.task
def user_created(user_id):

    user = CustomizeUser.objects.get(id=user_id)
    subject = 'User nr. {}'.format(user_id)
    message = 'Dear {},\n\nYou have successfully create an account.\
                Your acc id is {}.'.format(user.first_name, user.id)
    mail_sent = send_mail(subject,
                          message,
                          'crazydemon713@gmail.com',
                          [user.email])
    return mail_sent