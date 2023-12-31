# Generated by Django 4.2.4 on 2023-08-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img_alter_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.TextField(default='exi', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]
