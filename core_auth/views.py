from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .PayZenFormToolBox import PayZenFormToolBox
import calendar
import time
import logging

logger = logging.getLogger()

payzenTB = PayZenFormToolBox(
    '15302382',  # shopId
    'h38uqSOfPrF1xtZd',  # certificate, TEST-version
    '',  # certificate, PRODUCTION-version
    'TEST',               # TEST-mode toggle
    logger                # logger object the toolbox must use
)

ipn_url = 'https://lilsunrise.pythonanywhere.com/core_auth/form_ipn/'
payzenTB.ipn_url = ipn_url

return_url = 'https://lilsunrise.pythonanywhere.com/core_auth/return_from_payment/'
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



from django.shortcuts import render

def success_view(request):
    return render(request, 'success.html')

def error_view(request):
    return render(request, 'error.html')

def cancel_view(request):
    return render(request, 'cancel.html')
