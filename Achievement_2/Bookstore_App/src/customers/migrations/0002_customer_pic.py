# Generated by Django 4.2 on 2023-05-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='customers'),
        ),
    ]
