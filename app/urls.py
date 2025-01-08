from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('data_base/', views.data_base, name='data_base'),  # Маршрут для data_base.html
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('data_table/', views.data_table, name='data_table'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('delete_service_record/<int:record_id>/', views.delete_service_record, name='delete_service_record'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('edit_service_record/<int:record_id>/', views.edit_service_record, name='edit_service_record'),
]
