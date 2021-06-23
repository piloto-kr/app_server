from django.db import models

class Userinfo(models.Model):
    uuid        = models.CharField(max_length=40, verbose_name="UUID")
    parentName  = models.CharField(max_length=10, verbose_name="양육자 이름")
    parentAge   = models.IntegerField(default=0, verbose_name="양육자 나이")
    relation    = models.CharField(max_length=10, verbose_name="아이와 관계")
    familyName  = models.CharField(max_length=10, verbose_name="아이 성")
    childName   = models.CharField(max_length=10, verbose_name="아이 이름")
    childMonths = models.IntegerField(default=0, verbose_name="아이 개월수")
    childSex    = models.CharField(max_length=10, verbose_name="아이 성별")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.uuid

    class Meta:
        db_table            = 'userinfo'
        verbose_name        = '사용자 정보'
        verbose_name_plural = '사용자 정보'
