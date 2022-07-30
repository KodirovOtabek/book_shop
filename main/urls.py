from django.urls import path
from . import views
from .models import Book


urlpatterns = [
    path('', views.index, name='home'),
    path('О нас', views.about, name='about'),
    path('Жанр', views.category_of_books, name='genre'),
    path('Список книг', views.list_of_books, name='list'),
    path('<str:cb>', views.get_full_category),
    path('book/<slug:books_detail>/', views.category_url, name='books_detail'),
    path('cart/', views.get_user_cart, name='cart'),
    path('del_item/<int:pk>/', views.delete_item_from_cart),
]


