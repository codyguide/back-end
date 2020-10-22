from django.db import models
from django.db import models
from django.contrib.auth.models import User
from member.models import User
from member.models import Person


class Gallery(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=500, null=False)
    img_path = models.FileField(max_length=200, null=False)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = 'gallery'
        ordering = ['-created']
