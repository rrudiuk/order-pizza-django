# Generated by Django 3.0.7 on 2020-06-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200604_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='extra',
            field=models.ManyToManyField(blank=True, related_name='extra', to='orders.SubExtra'),
        ),
    ]
