# Generated by Django 2.2.14 on 2021-09-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210904_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.AddField(
            model_name='itemimage',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
