# Generated by Django 4.1.2 on 2022-10-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('categoriya', models.CharField(max_length=30, verbose_name='Категория')),
                ('vozrast', models.CharField(max_length=30, verbose_name='Возраст')),
                ('otsrochka', models.CharField(max_length=30, verbose_name='Наличие отстрочки')),
                ('adress', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
        ),
    ]
