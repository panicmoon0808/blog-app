# Generated by Django 2.2.3 on 2019-07-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='instructions',
            field=models.TextField(default='blank'),
            preserve_default=False,
        ),
    ]
