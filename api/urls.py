from django.urls import path
from .views import TodoGetCreate, TodoUpdateDelete,TodoDeleteView,TodoEditView, TodoDetailView
from api import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create',views.create, name='create'),
    path(r'todo/done/<int:pk>', views.isDone, name='done'),
    path(r'todo/delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
    path(r'todo/edit/<int:pk>', TodoEditView.as_view(), name='edit'),
    path(r'todo/detail/<int:pk>', TodoDetailView.as_view(), name='detail'),
    path('api/create',TodoGetCreate.as_view()),
    path(r'<int:pk>', TodoUpdateDelete.as_view()),
]