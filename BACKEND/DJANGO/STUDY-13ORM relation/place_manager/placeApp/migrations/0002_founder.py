# Generated by Django 5.0.6 on 2024-05-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
