from django.db import models

class Feedback(models.Model):
    months      = models.IntegerField(default=0, verbose_name="개월수")
    sex         = models.CharField(max_length=4, verbose_name="성별")
    feedback    = models.TextField(verbose_name="의견")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.feedback

    class Meta:
        db_table            = 'feedback'
        verbose_name        = 'Feedback'
        verbose_name_plural = 'Feedback'
