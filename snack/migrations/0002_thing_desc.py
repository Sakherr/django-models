# Generated by Django 4.2.3 on 2023-07-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='desc',
            field=models.TextField(default='no desc available'),
        ),
    ]