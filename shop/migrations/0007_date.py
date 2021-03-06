# Generated by Django 2.2.14 on 2021-07-24 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('dele', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
    ]
