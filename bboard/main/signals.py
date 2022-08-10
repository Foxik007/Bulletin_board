from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bb


#@receiver(post_save,sender=Bb)
#def save_bb(sender, instance, created, **kwargs):
#    делаем что то по при сохранении обьявления