from django.db import models


class Bargain(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование торга')
    date = models.DateTimeField(verbose_name='Дата проведения')
    placement_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
    source = models.CharField(max_length=250, blank=True, verbose_name='Источник')

    class Meta:
        verbose_name = 'Торг'
        verbose_name_plural = 'Торги'

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование документа')
    placement_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
    source = models.CharField(max_length=250, blank=True, verbose_name='Источник')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title
