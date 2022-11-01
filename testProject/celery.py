
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging
import datetime

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testProject.settings')

app = Celery('testProject', broker='redis://127.0.0.1:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# send mail task 
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


@shared_task(bind=True)
def sendMailToAdminWithCelery(self):
    User = get_user_model()

    print ("test")
    adminEmailList = User.objects.filter(is_superuser = True , is_active = True ).exclude(email__isnull=True).exclude(email="").values_list('email', flat=True)    
    subject = 'created new item'
    message = ' new product added '
    email_from = 'rightel.test.mail@gmail.com'
    try:
        send_mail( subject, message, email_from, adminEmailList )
        logger.info(
            f"email send to {adminEmailList}" + str(datetime.datetime.now()),
            )
    except:
        logger.info(
            f"dont send mail to {adminEmailList}" + str(datetime.datetime.now()),
            )
        return('dont send mail :(')
    return('task_done')


    