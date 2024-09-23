from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Post


# Pre-save signal
@receiver(pre_save, sender=Post)
def pre_save_post(sender, instance, **kwargs):
    print(f"Pre-save signal triggered for: {instance.title}")

# Post-save signal
@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if created:
        print(f"New post created: {instance.title}")
    else:
        print(f"Post updated: {instance.title}")

# Pre-delete signal
@receiver(pre_delete, sender=Post)
def pre_delete_post(sender, instance, **kwargs):
    print(f"Pre-delete signal triggered for: {instance.title}")

# Post-delete signal
@receiver(post_delete, sender=Post)
def post_delete_post(sender, instance, **kwargs):
    print(f"Post deleted: {instance.title}")
