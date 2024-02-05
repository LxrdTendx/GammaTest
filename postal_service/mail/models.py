from django.db import models

class LetterType(models.IntegerChoices):
    LETTER = 1, 'Письмо'
    REGISTERED_LETTER = 2, 'Заказное письмо'
    VALUABLE_LETTER = 3, 'Ценное письмо'
    EXPRESS_LETTER = 4, 'Экспресс-письмо'

class ParcelType(models.IntegerChoices):
    SMALL_PACKET = 1, 'Мелкий пакет'
    PARCEL = 2, 'Посылка'
    FIRST_CLASS_PARCEL = 3, 'Посылка 1 класса'
    VALUABLE_PARCEL = 4, 'Ценная посылка'
    INTERNATIONAL_PARCEL = 5, 'Посылка международная'
    EXPRESS_PARCEL = 6, 'Экспресс-посылка'

class Letter(models.Model):
    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    sending_point = models.CharField(max_length=255)
    receiving_point = models.CharField(max_length=255)
    sending_index = models.IntegerField()
    receiving_index = models.IntegerField()
    letter_type = models.IntegerField(choices=LetterType.choices)
    weight = models.IntegerField()

class Parcel(models.Model):
    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    sending_point = models.CharField(max_length=255)
    receiving_point = models.CharField(max_length=255)
    sending_index = models.IntegerField()
    receiving_index = models.IntegerField()
    notification_phone = models.CharField(max_length=20)
    parcel_type = models.IntegerField(choices=ParcelType.choices)
    payment_amount = models.IntegerField()
