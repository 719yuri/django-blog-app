from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 200)
  content = models.TextField
  create_at = models.DateTimeField
  update_at = models.DateTimeField
  is_published = models.BooleanField #wakaranu~~~!
