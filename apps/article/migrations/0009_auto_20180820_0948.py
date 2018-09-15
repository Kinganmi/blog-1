# Generated by Django 2.0.6 on 2018-08-20 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180815_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名字')),
                ('image', models.ImageField(default='article/subject/default.png', help_text='350x170', max_length=200, upload_to='article/subject/%Y/%m', verbose_name='封面')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '专题',
                'verbose_name_plural': '专题',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='article/image/default.png', help_text='160x120', max_length=200, upload_to='article/image/%Y/%m', verbose_name='文章缩略图'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.ImageField(default='img/avatar/default.png', max_length=200, upload_to='img/avatar/%Y/%m', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='commentreplay',
            name='avatar',
            field=models.ImageField(default='img/avatar/default.png', max_length=200, upload_to='img/avatar/%Y/%m', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='article',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_subject', to='article.Subject', verbose_name='专题'),
        ),
    ]
