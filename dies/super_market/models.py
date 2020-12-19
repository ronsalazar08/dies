from django.db import models

class records(models.Model):
    part_id = models.CharField(max_length=50)
    model_id = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    status_id = models.BooleanField(default=False)
    car_model = models.CharField(max_length=50, default='')
    machine_no = models.CharField(max_length=50, default='')
    mfg_div = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.part_id)

    class Meta:
        verbose_name_plural = "Records"
    