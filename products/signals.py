from django.db.models import signals
from .models import ProductModel
from django.dispatch import receiver
from testProject.celery import sendMailToAdminWithCelery

@receiver(signals.pre_save, sender=ProductModel)
def sendMailToAdmin(**kwargs):
    sendMailToAdminWithCelery.delay()






