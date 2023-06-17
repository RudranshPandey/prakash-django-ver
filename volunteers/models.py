from django.db import models

# Create your models here.
class volunteer_profiles(models.Model):
    GENDER_LISTS=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=GENDER_LISTS)
    phone_number = models.IntegerField(default=0)
    ngo_association = models.CharField(max_length=100)
    area_of_operation = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Volunteer Profile"
    
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.phone_number}"