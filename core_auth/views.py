from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PayZenFormToolBox import PayZenFormToolBox
import calendar
import time
import logging

logger = logging.getLogger()

payzenTB = PayZenFormToolBox(
    '28321394',  # shopId
    'JTa3Ix5RxInDOD2P',  # certificate, TEST-version
    # '[***CHANGE-ME***]',  # certificate, PRODUCTION-version
    'TEST',               # TEST-mode toggle
    logger                # logger object the toolbox must use
)

ipn_url = '/form_ipn/'
payzenTB.ipn_url = ipn_url

return_url = '/return_from_payment/'
payzenTB.return_url = return_url

def form_payment(request):
    amount = 1000  # payment amount
    currency = 978  # payment currency code
    trans_id = str(calendar.timegm(time.gmtime()))[-6:]  # unique transaction id

    form = payzenTB.form(trans_id, amount, currency)

    return render(request, 'form_payment.html', {'form': form})

@csrf_exempt
def form_ipn(request):
    try:
        data = request.POST
        response = payzenTB.ipn(data)
        # Handle different payment statuses here
        return HttpResponse('Notification processed!')
    except:
        return HttpResponse(status=500)

def return_from_payment(request):
    return HttpResponse("Welcome back, dear Customer!")

def test_transaction(request):
    # Générer un ID de transaction unique
    trans_id = str(calendar.timegm(time.gmtime()))[-6:]

    # Données de paiement fictives
    amount = 1000  # Montant du paiement
    currency = 978  # Code de la devise

    # Créer un formulaire de paiement avec les données fictives
    form = payzenTB.form(trans_id, amount, currency)

    # Simuler l'envoi des données à l'API de PayZen (c'est ici que tu enverrais réellement les données)

    # Retourner une réponse JSON avec le formulaire de paiement
    return JsonResponse({'form': form})