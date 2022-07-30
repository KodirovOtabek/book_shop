from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import SearchForm, RegisterForm
from .handlers import bot


def index(request):
    books = Book.objects.order_by('-id')[:8]
    categories = Category.objects.all()
    search_bar = SearchForm()
    context = {
        'title': 'Главная страница',
        'books': books,
        'form': search_bar
    }

    if request.method == 'POST':
        book_to_find = request.POST.get('search_book')

        try:
            search_result = Book.objects.get(book_work=book_to_find)
            return redirect(f'/book/{search_result.slug}/')
        except:
            return redirect('/')
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def category_of_books(request):
    categories = Category.objects.all()
    return render(request, 'main/categories.html', {'categories': categories})


def list_of_books(request):
    books = Book.objects.all()

    return render(request, 'main/list.html', {'books': books})


def category_url(request, books_detail):
    args = {}
    args['books_detail'] = get_object_or_404(Book, slug=books_detail)

    if request.method == 'POST':
        Cart.objects.create(user_id=request.user.id, user_book=args['books_detail'],
                            user_book_quantity=request.POST.get('book_quantity'))

        return redirect('/')

    return render(request, "main/books_detail.html", args)


def get_full_category(request, cb):
    get_category_id = Category.objects.get(category_name=cb)
    all_books = Book.objects.filter(book_category=get_category_id.id)

    return render(request, 'main/category_books.html',
                  {'books': all_books, 'category_name': get_category_id.category_name})


def get_user_cart(request):
    user_cart = Cart.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Новый заказ\n\n'

        for i in user_cart:
            main_text += f'Товар: {i.user_book} Количество: {i.user_book_quantity}\n'

        bot.send_message('2867129', main_text)

        return redirect('/')

    return render(request, 'main/user_cart.html', {'cart': user_cart})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

def delete_item_from_cart(request, pk):
    user_cart = Cart.objects.filter(user_id=request.user.id, user_book=pk)
    user_cart.delete()

    return redirect('/cart/')