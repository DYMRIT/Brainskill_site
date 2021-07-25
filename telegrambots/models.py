from django.db import models


class TeleSetting(models.Model):
    token = models.CharField(max_length=200, verbose_name='Токен')
    chat_id = models.CharField(max_length=200, verbose_name='чат id')
    text = models.TextField(verbose_name='Текст отправки')

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'


class Order(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст формы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Форма помощи'
        verbose_name_plural = 'Формы помощи'