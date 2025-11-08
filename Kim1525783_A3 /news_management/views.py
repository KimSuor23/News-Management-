from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, News
from .forms import NewsForm

from django.contrib.auth.decorators import login_required


# show home page with latest news
def home(request):
    try:
        news = News.objects.order_by('-published_date')[:4]
        return render(request, "news_management/home.html", {"news": news})
    except Exception as e:
        return HttpResponse("error loading home page")

# show all categories
def category_list(request):
    try:
        categories = Category.objects.all()
        return render(request, "news_management/categories.html", {"categories": categories})
    except Exception:
        return HttpResponse("error loading categories")

# show news for one category
def category_detail(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        news = News.objects.filter(category=category).order_by('-published_date')
        return render(request, "news_management/category_detail.html", {"category": category, "news": news})
    except Exception:
        return HttpResponse("error showing category")

# show single article
def article_detail(request, pk):
    try:
        article = get_object_or_404(News, pk=pk)
        return render(request, "news_management/article_detail.html", {"article": article})
    except Exception:
        return HttpResponse("error loading article")

# Create news - CRUD
@login_required
def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news_management/news_form.html', {'form': form})

# Update news - CRUD
@login_required
def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=news.pk)  # note: use article_detail in urls.py
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_management/news_form.html', {'form': form})

# Delete news - CRUD
@login_required
def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        news.delete()
        return redirect('home')
    return render(request, 'news_management/news_confirm_delete.html', {'news': news})
