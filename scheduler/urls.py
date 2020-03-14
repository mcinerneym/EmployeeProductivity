from django.urls import path

from . import views

app_name = 'scheduler'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ShiftView.as_view(), name='shift'),
    path('<int:employee_id>/addShift/', views.addShift, name='addShift'),
    path('<int:employee_id>/showShift/<int:shift_id>', views.showShift, name='showShift'),
    path('<int:employee_id>/editShift/<int:shift_id>', views.editShift, name='editShift'),
    path('dayStatus', views.getDayStatus, name='dayStatus'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
]