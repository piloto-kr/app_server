from django.db import models

class Pit(models.Model):
    uuid        = models.CharField(max_length=40, verbose_name="UUID")
    pit_type    = models.CharField(max_length=40, verbose_name="검사 항목")
    checklist   = models.CharField(max_length=40, verbose_name="검사 결과")
    content     = models.CharField(max_length=200, verbose_name="응답 내용")
    checked_at  = models.DateTimeField(auto_now_add=True, verbose_name="검사일")

    def __str__(self):
        return self.uuid
        
    class Meta:
        db_table            = 'pit'
        verbose_name        = 'Piloto Integrated Test'
        verbose_name_plural = 'Piloto Integrated Test'
        