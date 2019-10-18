from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.db import models
class UserInfo(models.Model):
    uname=models.CharField(max_length=10)
    upwd=models.CharField(max_length=40)
    isDelete=models.BooleanField()
# Register your models here.
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcomment=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
class Test1(models.Model):
    content=HTMLField()