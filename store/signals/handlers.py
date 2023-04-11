from ..models import Customer
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
# NOW, auth_user_model knows that when the user is created this method will called.
def create_customer_for_new_user(sender,**kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance']) 