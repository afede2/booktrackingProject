from django.urls import path, include
from . import views
from . views import in_progress_book

urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:user_id>/in-progress', in_progress_book, name='in_progress_books')
]