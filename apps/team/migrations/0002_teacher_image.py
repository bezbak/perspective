# Generated by Django 4.1.7 on 2023-03-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=1, upload_to='team/'),
            preserve_default=False,
        ),
    ]