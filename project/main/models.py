from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title


class Objavlenie(models.Model):
    adress = models.CharField('Адрес', max_length=50)
    price = models.TextField('Цена')
    decribe = models.TextField('Описание')
    count_room = models.TextField('Кол-во комнат')
    type_hous = models.TextField('Тип дома')
    img = models.ImageField('Фото')



    def __str__(self):
        return self.adress


class Employ(models.Model):
    name = models.CharField('ФИО', max_length=50)
    img = models.ImageField('Фотка')
    age = models.TextField('Возраст')
    major = models.TextField('Специальность')
    staz = models.TextField('Стаж')
    salary = models.TextField('ЗП')


    def __str__(self):
        return self.name