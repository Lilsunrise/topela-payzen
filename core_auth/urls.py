from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_transaction, name='test_transaction'),
    path('form_ipn/', views.form_ipn, name='form_ipn'),
    path('return_from_payment/', views.return_from_payment, name='return_from_payment'),
    # Ajoute d'autres URLs si nécessaire
]