# Generated by Django 2.0.6 on 2018-08-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180815_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='qq',
        ),
        migrations.RemoveField(
            model_name='commentreplay',
            name='qq',
        ),
        migrations.AddField(
            model_name='comment',
            name='avatar',
            field=models.ImageField(default='img/avatar/man_5.png', max_length=200, upload_to='img/avatar/%Y/%m', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='comment',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='commentreplay',
            name='avatar',
            field=models.ImageField(default='img/avatar/man_5.png', max_length=200, upload_to='img/avatar/%Y/%m', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='commentreplay',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
        ),
    ]
