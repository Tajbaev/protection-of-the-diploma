from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CommentModel(models.Model):
    title = models.CharField('TITLE', max_length=250)
    content = models.TextField('CONTENT', max_length=500)
    img = models.ImageField('Картинка', upload_to='comment/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'