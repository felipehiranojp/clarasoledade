# Generated by Django 5.1 on 2024-09-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabela',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
