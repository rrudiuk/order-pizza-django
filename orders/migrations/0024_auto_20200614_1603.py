# Generated by Django 3.0.7 on 2020-06-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20200614_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='hash_name',
            field=models.CharField(default='some', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
