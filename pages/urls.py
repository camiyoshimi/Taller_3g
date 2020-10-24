from django.urls import path
from . import views
from pages.views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

urlpatterns = [
    #path('', views.pages, name='pages'),
    path('pages/', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
]