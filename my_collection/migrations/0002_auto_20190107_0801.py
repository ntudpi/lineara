# Generated by Django 2.1.5 on 2019-01-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='drawing',
            field=models.ImageField(upload_to='./media'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='./media'),
        ),
        migrations.AlterField(
            model_name='item',
            name='transcription',
            field=models.ImageField(upload_to='./media'),
        ),
    ]
