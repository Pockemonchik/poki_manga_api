from django.db import models

# Create your models here.

class Manga(models.Model):
    """Класс для шаблонов документов Сводок"""
    name = models.CharField(max_length=50, null=True, blank=True)
   

    class Meta:
        verbose_name = "Mанга"
        verbose_name_plural = "Манги"
        ordering = ["-name"]
    
    def __str__(self):
        try:
            return self.name
        except:
            return str(self.id)