from django.db import models
from django.utils import timezone

# Create your models here.
class PlayList(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class Video(models.Model):
    plist = models.ForeignKey(PlayList,on_delete = models.CASCADE)
    title = models.CharField(max_length= 200)
    vid = models.CharField(max_length=20)

    def __str__(self):
        return self.title
