from django.db import models
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    big_image = FilerImageField(verbose_name='Большое изображение',
                                blank=True, null=True,
                                on_delete=models.CASCADE,
                                related_name='big_slider_images')
    image = FilerImageField(verbose_name='Изображение',
                            blank=True, null=True,
                            on_delete=models.CASCADE,
                            related_name='slider_images')
    title = models.CharField(max_length=255, verbose_name='Название')
    my_order = models.PositiveIntegerField(verbose_name='Поле для сортировки',
                                           default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Элементы слайдера'

    def __str__(self):
        return self.title
