from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    poll = models.ForeignKey('webapp.Poll', related_name='polls_choice',
                             on_delete=models.CASCADE, null=False, blank=False, verbose_name='Опрос')

    def __str__(self):
        return self.text


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='polls_answer',
                             on_delete=models.PROTECT, null=False, blank=False, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice = models.ForeignKey('webapp.Choice', related_name='choices_answer', on_delete=models.PROTECT,
                               null=False, blank=False, verbose_name='Вариант ответа')
