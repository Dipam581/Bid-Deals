# Generated by Django 5.0.7 on 2024-08-04 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creationdata',
            name='image',
        ),
    ]
