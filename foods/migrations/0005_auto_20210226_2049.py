# Generated by Django 3.1.6 on 2021-02-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20210226_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('drinks', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'ناهار')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
