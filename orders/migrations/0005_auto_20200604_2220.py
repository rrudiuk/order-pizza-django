# Generated by Django 3.0.7 on 2020-06-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200604_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='extra',
            field=models.ManyToManyField(blank=True, to='orders.SubExtra'),
        ),
    ]
