# Generated by Django 4.1.2 on 2022-10-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
