# core/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    
    # New fields for admit card
    exam_name = models.CharField(max_length=100, blank=True, null=True)
    exam_date = models.DateField(blank=True, null=True)
    exam_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"


# Create profile if user is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# # Save profile only if it exists (avoid crashing for admin)
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     try:
#         instance.profile.save()
#     except Profile.DoesNotExist:
#         pass
