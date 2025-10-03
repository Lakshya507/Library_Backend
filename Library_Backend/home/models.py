import random
from django.db import models
from django.contrib.auth.models import User

def generate_token():
    return ''.join(random.choices('0123456789', k=4))

class ShelfToken(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('assigned', 'Assigned'),
        ('retrieval_requested', 'Retrieval Requested'),
        ('collected', 'Collected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shelf_number = models.PositiveIntegerField()
    token = models.CharField(max_length=4, unique=True, default=generate_token)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')

    def __str__(self):
        return f"{self.user.username} → Shelf {self.shelf_number} ({self.get_status_display()})"
