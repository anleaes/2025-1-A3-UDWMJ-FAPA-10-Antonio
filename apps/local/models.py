from django.db import models

class Local(models.Model):
    endereco = models.CharField(max_length=255, verbose_name="Endereço Completo")
   
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"
        ordering = ['endereco']

    def __str__(self):
        return self.endereco