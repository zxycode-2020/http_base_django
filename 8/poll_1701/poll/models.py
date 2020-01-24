#coding:utf8
from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

from django.db import models
class Question(models.Model): # 投票主题表
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #添加日期

    def was_published_recently(self):  # 是否是最近一天内添加的投票
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '是否最近一天内添加？'


    def __unicode__(self):
        return self.question_text

class Choice(models.Model):  #投票选项表
    question = models.ForeignKey(Question) # 投票主题ID
    choice_text = models.CharField(max_length=200) # 选项内容
    votes = models.IntegerField(default=0) # 票数


    def __unicode__(self):
        return self.choice_text