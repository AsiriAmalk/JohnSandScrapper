# Generated by Django 3.0.3 on 2020-06-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reals', '0004_auto_20200604_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='priority',
            field=models.BooleanField(default=False),
        ),
    ]
