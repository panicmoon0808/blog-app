# Generated by Django 2.2.3 on 2019-07-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(to='blog.Comment', verbose_name='Comment'),
        ),
    ]
