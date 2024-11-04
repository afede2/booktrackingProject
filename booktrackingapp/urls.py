from django.urls import path, include
from . import views
from . views import to_read_book, in_progress_book, completed_book

urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:user_id>/to-read', to_read_book, name='to_read_book'),
    path('users/<int:user_id>/in-progress', in_progress_book, name='in_progress_books'),
    path('users/<int:user_id>/completed', completed_book, name='completed_book')


]