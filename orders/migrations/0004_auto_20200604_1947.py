# Generated by Django 3.0.7 on 2020-06-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_subextra_subs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('size', models.CharField(choices=[('L', 'L'), ('S', 'S')], max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('extra', models.ManyToManyField(blank=True, related_name='extra', to='orders.SubExtra')),
            ],
        ),
        migrations.DeleteModel(
            name='Subs',
        ),
    ]
