# Generated by Django 2.2.14 on 2021-09-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210905_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='memory',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
