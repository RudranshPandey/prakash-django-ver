from django.db import models
from django.utils.html import mark_safe
import shortuuid
# Create your models here.
class All_profiles(models.Model):
    GENDER_LISTS=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER')
    )
    id = models.CharField(max_length=22, primary_key=True, default=shortuuid.uuid, editable=False)
    memo_no = models.CharField(max_length=50,default="",blank =True)
    first_name = models.CharField(max_length=50,default="",blank=True)
    last_name = models.CharField(max_length=50, default="", blank=True)
    age = models.IntegerField(default="",blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_LISTS,blank=True)
    ngo_assigned = models.CharField(max_length=100,default="",blank=True)
    description = models.CharField(max_length=1000)
    pickup_location = models.CharField(max_length=1000)
    pickup_date = models.DateTimeField()
    Image = models.ImageField(upload_to="victims/images",default="")

    class Meta:
        verbose_name = "All Profile"

    def __str__(self):
        return f"{self.memo_no},{self.pickup_location}"

    def imgpreview(self):
        return mark_safe(f'<img src = "{self.Image.url}" width = "300"/>')