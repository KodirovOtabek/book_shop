from django.db import models
import uuid
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField('Название категории',max_length=300)
    category_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Book(models.Model):
    book_work = models.CharField('Произведение', max_length=500)
    slug = models.CharField(max_length=100, unique=True, verbose_name='url', default=uuid.uuid4)
    book_author = models.CharField('Автор', max_length=500)
    book_description = models.TextField('Описание')
    book_price = models.FloatField('Цена')
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    book_photo = models.ImageField(upload_to='images/')
    book_quantity = models.IntegerField('Количество', blank=True, null=True)
    book_date = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('books_detail', args=[self.slug])

    def __str__(self):
        return self.book_work

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

class Cart(models.Model):
    user_id = models.IntegerField()
    user_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_book_quantity = models.IntegerField()

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
