# Generated by Django 3.2.19 on 2023-05-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victims', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_no', models.CharField(blank=True, default='', max_length=50)),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20)),
                ('ngo_assigned', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('pickup_location', models.CharField(blank=True, default='', max_length=1000)),
                ('pickup_date', models.DateTimeField()),
                ('Image', models.ImageField(default='', upload_to='human_profile/images')),
            ],
            options={
                'verbose_name': 'All Profile',
            },
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
    ]
