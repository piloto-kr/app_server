from django.db import models

class Harmful(models.Model):
    uuid        = models.CharField(max_length=40, verbose_name="UUID")
    date        = models.CharField(max_length=10, verbose_name="날짜")
    wordSet    = models.CharField(max_length=100, verbose_name="차단 단어")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.wordSet

    class Meta:
        db_table            = 'harmful'
        verbose_name        = '유해차단'
        verbose_name_plural = '유해차단'
