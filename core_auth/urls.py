from django.urls import path
from . import views

urlpatterns = [
    path('form_payement/', views.form_payment, name="form_payment"),
    path('form_ipn/', views.form_ipn, name='form_ipn'),
    path('return_from_payment/', views.return_from_payment, name='return_from_payment'),
    path('success/', views.success_view, name='payment_success'),
    path('error/', views.error_view, name='payment_error'),
    path('cancel/', views.cancel_view, name='payment_cancel'),
    # Ajoute d'autres URLs si nécessaire
]