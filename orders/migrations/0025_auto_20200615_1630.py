# Generated by Django 3.0.7 on 2020-06-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200614_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='topping1',
            field=models.CharField(default='empty', max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='topping2',
            field=models.CharField(default='empty', max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='topping3',
            field=models.CharField(default='empty', max_length=64),
        ),
        migrations.AddField(
            model_name='topping',
            name='hash_name',
            field=models.CharField(default='some', max_length=64),
            preserve_default=False,
        ),
    ]
