from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    user_upload_image = [
        ('rm','random'),
        ('sf','self'),
        ('gf','girlfrend'),
    ]
    comment=models.TextField(max_length=500)
    image = models.ImageField(upload_to='abhay/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=user_upload_image)