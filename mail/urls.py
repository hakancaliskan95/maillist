from django.urls import path
from .views import IndexView, ListView, AddView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list', ListView.as_view(), name='list'),
    path('add', AddView.as_view(), name='add'),
]