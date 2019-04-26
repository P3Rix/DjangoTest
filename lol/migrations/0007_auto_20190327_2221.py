# Generated by Django 2.1.7 on 2019-03-27 22:21

from django.db import migrations, models
import lol.models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0006_auto_20190327_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userlevel',
            field=models.CharField(default='User', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='model_pic',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to=lol.models.function),
        ),
    ]
