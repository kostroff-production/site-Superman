# Generated by Django 2.1.5 on 2019-04-25 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['slug']},
        ),
    ]
