# Generated by Django 3.1.6 on 2021-03-12 08:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='متن'),
        ),
    ]
