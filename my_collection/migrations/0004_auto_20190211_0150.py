# Generated by Django 2.1.5 on 2019-02-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_collection', '0003_auto_20190107_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='drawing',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='drawing'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='transcription',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='transcription'),
        ),
    ]
