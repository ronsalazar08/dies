from django.db import models
# from super_market.models import records as super_records
from django.contrib.auth import authenticate

class records(models.Model):
    model_id = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    def __str__(self):
        return str(self.part_number)

    class Meta:
        verbose_name_plural = "Records"

    # def save(self, *args, **kwargs):
        # user = authenticate(username='admin', password='admin1')
        # if user is not None:
        #     print('admin')
        # else:
        #     print('not admin')
        # super_item = super_records.objects.filter(part_number=olo[0], model_id=olo[1], status_id=False)
        pass
