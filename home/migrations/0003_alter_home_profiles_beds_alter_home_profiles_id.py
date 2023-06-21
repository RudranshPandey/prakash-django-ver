# Generated by Django 4.2.1 on 2023-06-19 15:42

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_home_profiles_delete_volunteer_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_profiles',
            name='beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='home_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]