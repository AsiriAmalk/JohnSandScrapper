# Generated by Django 3.0.3 on 2020-06-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=512)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('beds', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('link', models.CharField(max_length=1083)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]