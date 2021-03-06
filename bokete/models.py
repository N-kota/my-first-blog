import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
def __str__(self):
        return self.question_text

def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    class Meta:
        verbose_name = "お題"
        verbose_name_plural = "お題"

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Image(models.Model):
    question = models.ForeignKey(Question, verbose_name='question',blank=True, null=True,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
