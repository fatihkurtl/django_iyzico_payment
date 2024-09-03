from django.shortcuts import render
from django.views.generic import View
from .helper import PaymentProvider


class PaymentView(View):

    def get(self, request):
        return render(request, "pages/payment.html")
    
    def post(self, request):
        payment = PaymentProvider(data=request.POST).make_payment()
        if payment['success'] == True:
            print('Ödeme İşlemi Başarıyla Tamamlandı')
        else:
            print('Ödeme İşleminde Hata Meydana Geldi')  
        return render(request, "pages/payment.html")