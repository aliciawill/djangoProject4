from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ", " + self.title + ", " + self.content + ", " + self.writer

class Reply(models.Model):
    bid = models.IntegerField()
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ", " + str(self.bid) + ", " + self.content + ", " + self.writer
