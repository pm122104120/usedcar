from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
SEX_CHOICES = (
    (0,'男'),
    (1,'女'),
)

ROLE_CHOICES = (
    (0,'buy'),
    (1,'sale'),
    (2,'back'),
)

BANK_CHOICES = (
    (0,'中国工商银行'),
    (1,'中国建设银行'),
    (2,'中国农业银行'),
    (3,'招商银行'),
    (4,'北京银行'),
    (5,'我家银行'),
)

class UserInfo(AbstractUser):
    realname = models.CharField('真实姓名',max_length=30,null=False)
    iden = models.CharField('身份证号',max_length=18,null=False)
    ads = models.CharField('地址',max_length=200,null=False)
    uphone = models.CharField('手机号',max_length=20,null=False)
    sex = models.IntegerField(verbose_name='性别',choices=SEX_CHOICES,default=0)
    role = models.IntegerField(verbose_name='角色',choices=ROLE_CHOICES,default=0)
    isActive = models.BooleanField(verbose_name='是否激活',default=False)
    isBan = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.username

class Bank(models.Model):
    cardNo = models.CharField('卡号',max_length=30,null=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    cpwd = models.CharField('交易密码',max_length=200,null=False)
    bank = models.IntegerField(verbose_name='开户银行',choices=BANK_CHOICES,default=0)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.user.username

