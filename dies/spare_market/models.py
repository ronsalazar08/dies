from django.db import models

class records(models.Model):
    model_id = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    def __str__(self):
        return str(self.part_number)

    class Meta:
        verbose_name_plural = "Records"