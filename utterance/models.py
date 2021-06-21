from django.db import models

class Utterance(models.Model):
    months      = models.IntegerField(default=0, verbose_name="개월수")
    sex         = models.CharField(max_length=4, verbose_name="성별")
    question    = models.CharField(max_length=200, verbose_name="질문")
    answer      = models.CharField(max_length=200, verbose_name="대답")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="발화일")

    def __str__(self):
        return self.question

    class Meta:
        db_table            = 'utterance'
        verbose_name        = '발화내용'
        verbose_name_plural = '발화내용'
