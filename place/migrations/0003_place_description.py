# Generated by Django 2.2.2 on 2019-06-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20190617_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
