from django.db import models

class Survey(models.Model):
    months      = models.IntegerField(default=0, verbose_name="개월수")
    sex         = models.CharField(max_length=4, verbose_name="성별")
    answer      = models.CharField(max_length=100, verbose_name="답변")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.answer

    class Meta:
        db_table            = 'survey'
        verbose_name        = '설문결과'
        verbose_name_plural = '설문결과'
