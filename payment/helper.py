import json
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv
import iyzipay

load_dotenv()

class PaymentProvider:
    def __init__(self, data):
        self.data = data
        self.full_name = data.get('full_name')
        self.card_number = data.get('card_number')
        self.expiration_date = data.get('card_expiration')
        self.cvc = data.get('cvc')
        
        self.base_url = os.environ.get('IYZICO_BASE_URL')
        self.iyzico_api_key = os.environ.get('IYZICO_API_KEY')
        self.iyzico_secret_key = os.environ.get('IYZICO_SECRET_KEY')
    
    def make_payment(self) -> Dict[str, Optional[str]]:
        if self.full_name and self.card_number and self.expiration_date and self.cvc:
            print(self.full_name, self.card_number, self.expiration_date, self.cvc)
            print(self.base_url, self.iyzico_api_key, self.iyzico_secret_key)
            
            options = {
                "base_url": self.base_url,
                "api_key": self.iyzico_api_key,
                "secret_key": self.iyzico_secret_key
            }
            
            payment_card = {
                "cardHolderName": self.full_name,
                "cardNumber": self.card_number,
                "expireMonth": self.expiration_date.split("/")[0],
                "expireYear": self.expiration_date.split("/")[1],
                "cvc": self.cvc,
                "registerCard": "0",
            }
            
            buyer = {
                "id": "BY789", # Alıcının ID'si
                "name": "John", # Alıcının adı
                "surname": "Doe", # Alıcının soyadı
                "gsmNumber": "+905350000000", # Alıcının telefon numarası
                "email": "3wzPv@example.com", # Alıcının e-posta adresi
                "identityNumber": "74300864791", # Alıcının kimlik numarası
                "lastLoginDate": "2015-10-05 12:43:35", # Alıcının son giriş tarihi
                "registrationDate": "2013-04-21 15:12:09", # Alıcının kayıt tarihi
                "registrationAddress": "Nidakule Goynuk, No:37", # Alıcının kayıtlı adresi
                "ip": "244.178.44.111", # Alıcının IP adresi
                "city": "Istanbul", # Alıcının yaşadığı şehir
                "country": "Turkey", # Alıcının yaşadığığı ülke
                "zipCode": "34732" # Alıcının posta kodu
            }
            
            address = {
                "contactName": "Jane Doe", # Adresle ilgili kişinin adı
                "city": "Istanbul", # Adresle ilgili kişinin sehiri
                "country": "Turkey", # Adresle ilgili kişinin ülkesi
                "address": "Nidakule Goynuk, No:37", # Adresle ilgili kişinin adresi
                "zipCode": "34742" # Adresle ilgili kişinin posta kodu
            }
            
            basket_items = [
                {
                    "id": "1", # Sepet öğesinin ID'si
                    "name": "Binocular", # Sepet öğesinin adı
                    "category1": "Collectibles", # Ana kategori
                    # "category2": "Accessories", # Alt kategori
                    "itemType": "PHYSICAL", # Ürün tipi
                    "price": "1", # Ürün fiyatı 
                    "quantity": "1" # Ürün adedi
                }
            ]
            
            request = {
                "locale": "tr", # Dil ve yerel ayar
                "conversationId": "123456789", # İsteğin konusma ID'si (genellikle benzersiz bir islem numarasi)
                "price": "1", #  Toplam tutar (vergiler haric)
                "paidPrice": "1.2", # Toplam odenen tutar (vergiler dahil)
                "currency": "TRY", # Para birimi
                "basketId": "B67832", # Sepetin ID'si
                "paymentChannel": "WEB", # Ödeme kanalı ('WEB' internet üzerinden ödeme icin)
                "paymentCard": payment_card, # Ödeme kartı bilgileri
                "buyer": buyer, # Alıcı bilgileri
                "shippingAddress": address, # Teslimat adresi
                "billingAddress": address, # Fatura adresi
                "basketItems": basket_items # Sepet ögeleri
            }
            
            payment = iyzipay.Payment().create(request, options)
            payment_result = payment.read().decode("UTF-8")
            for key, value in json.loads(payment_result).items():
                print(key, ":", value)
            
            return {
                "success": True
            }
        return {
            "success": False
        }
        pass
    
    def __call__(self):
        pass