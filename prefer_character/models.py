from django.db import models

class PreferCharacter(models.Model):
    uuid                = models.CharField(max_length=40, verbose_name="UUID")
    prefer_character    = models.JSONField(null=True)

    def __str__(self):
        return self.uuid

    class Meta:
        db_table            = 'prefer_character'
        verbose_name        = 'Prefer Character History'
        verbose_name_plural = 'Prefer Character History'
