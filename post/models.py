from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(verbose_name='Yorum')
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date']