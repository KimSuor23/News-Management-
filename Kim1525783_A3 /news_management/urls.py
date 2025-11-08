from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# url patterns for news management app
urlpatterns = [
    # home page showing latest news
    path('', views.home, name='home'),

    # page showing all categories
    path('categories/', views.category_list, name='category_list'),

    # page showing news inside one category, by category id
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),

    # page showing details of a single news article by id
    path('news/<int:pk>/', views.article_detail, name='article_detail'),

    # CRUD URLs for News model
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]
