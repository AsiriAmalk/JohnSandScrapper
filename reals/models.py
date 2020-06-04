from django.db import models

# Create your models here.

class Search(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    price = models.CharField(max_length=225)
    beds = models.CharField(max_length=3)
    bath = models.CharField(max_length=3)
    link = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = "Searches"

# title, address, price, number of beds (s), number of bath(s)