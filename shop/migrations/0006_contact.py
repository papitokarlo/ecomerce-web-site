# Generated by Django 2.2.14 on 2021-07-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210718_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.FloatField()),
                ('gmail', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
