# Generated by Django 2.2.14 on 2021-09-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_item_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='camera',
            new_name='maincamera',
        ),
        migrations.RemoveField(
            model_name='item',
            name='access',
        ),
        migrations.RemoveField(
            model_name='item',
            name='publish',
        ),
        migrations.AddField(
            model_name='item',
            name='frontcamera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='shida',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='systeminfo',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='memory',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='screen',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]