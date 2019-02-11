# Generated by Django 2.1.5 on 2019-01-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('drawing', models.ImageField(upload_to='')),
                ('transcription', models.ImageField(upload_to='')),
            ],
        ),
    ]