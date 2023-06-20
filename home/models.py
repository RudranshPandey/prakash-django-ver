from django.db import models
import shortuuid


# Create your models here.
class home_profiles(models.Model):
    CATEGORY_LISTS = (
        ('CORPORATION', 'CORPORATION'),
        ('PRIVATE', 'PRIVATE'),
        ('OTHER', 'OTHER')
    )
    id = models.CharField(max_length=22, primary_key=True, default=shortuuid.uuid, editable=False)
    home_name = models.CharField(max_length=50)
    home_address = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0)
    contact_person = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_LISTS)
    beds = models.IntegerField(default=0)

    class Meta:
        verbose_name = "home"

    def __str__(self):
        return f"{self.home_name},{self.home_address},{self.phone_number},{self.contact_person},{self.category},{self.beds}"