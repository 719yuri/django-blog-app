from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField('タイトル', max_length = 200)
  content = models.TextField()
  create_at = models.DateTimeField('更新日時', auto_now=True)
  update_at = models.DateTimeField('更新日時', auto_now=True)
  is_published = models.BooleanField
