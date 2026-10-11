from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('dashboard/', views.manager_dashboard, name='dashboard'),
    path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('update-stock/<int:book_id>/', views.update_book_stock, name='update_stock'),
    path('trigger-matrix-sync/', views.trigger_matrix_sync, name='trigger_matrix_sync'),
]
