from .models import Student
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete,sender=Student)
def delete_releted_user(sender, instance, **kwargs):
    print("releted user deleted")
    instance.user.delete()