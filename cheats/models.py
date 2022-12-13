from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    logo = models.ImageField(upload_to='logo', verbose_name='логотип')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


CHEAT_DRAFT = 'draft'
CHEAT_PUBLISHED = 'published'
CHEAT_EDITED = 'edited'


class Cheat(models.Model):
    STATUSES = (
        (CHEAT_DRAFT, 'черновик'),
        (CHEAT_PUBLISHED, 'опубликовано'),
        (CHEAT_EDITED, 'редактируется')
    )
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='текст')
    status = models.CharField(max_length=12, choices=STATUSES, verbose_name='статус')
    created_at = models.DateTimeField(auto_now=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='время редактирования')

    class Meta:
        verbose_name = 'шпаргалка'
        verbose_name_plural = 'шпаргалки'

    def __str__(self):
        return self.title
