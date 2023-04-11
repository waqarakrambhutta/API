from django.dispatch import receiver
from store.signals import order_created

@receiver(order_created)
def on_created_order(sender,**kwargs):
    print(kwargs)