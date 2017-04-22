from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

    #제목 보여주기
    #제목과 괄호 안에 조회수 보여주기 
    def __str__(self):
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=80)
