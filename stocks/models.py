from django.db import models


class Stock(models.Model):
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    name = models.CharField(max_length=30, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    categoriya = models.CharField(max_length=30, verbose_name="Категория")
    vozrast = models.CharField(max_length=30, verbose_name="Возраст")
    otsrochka = models.CharField(max_length=30, verbose_name="Наличие отстрочки")
    adress = models.CharField(max_length=100, verbose_name="Адрес")

    class Meta:
        managed = False
        db_table = 'prizivniki'
