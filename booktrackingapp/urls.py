from django.urls import path, include
from . import views
from .views import to_read, in_progress, completed, add_to_list, stats, journal_entry, create_entry

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-list', add_to_list, name='add_to_list'),
    path('to-read', to_read, name='to_read'),
    path('in-progress', in_progress, name='in_progress'),
    path('completed', completed, name='completed'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('stats', stats, name='stats'),

    path('journal_entry', views.journal_entry, name='journal_entry'),

    path('create_entry', create_entry, name='create_entry'),

]