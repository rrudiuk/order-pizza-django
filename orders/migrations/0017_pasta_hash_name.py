# Generated by Django 3.0.7 on 2020-06-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasta',
            name='hash_name',
            field=models.CharField(default='some', max_length=64),
            preserve_default=False,
        ),
    ]
