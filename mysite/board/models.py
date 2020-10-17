from django.db import models
from django.db import models
from django.contrib.auth.models import User
from member.models import User
from member.models import Person


class Board(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Types(models.TextChoices):
        QUESTION = "Q&A"
        TIP = "여행 TIP"
        POST = "자유 게시판"

    category = models.CharField(
        max_length=10, null=False, choices=Types.choices)
    title = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=500, null=False)
    img_path = models.FileField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = 'board'
        ordering = ['-created']


class Comment(models.Model):
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE)
    user = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    content = models.CharField(max_length=300,  null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'
        ordering = ['-created']
