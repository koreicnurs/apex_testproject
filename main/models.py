import base64

from django.db import models


class MainUser(models.Model):
    full_name = models.CharField('ФИО', max_length=200)
    phone_number = models.CharField('Номер телефона', max_length=20)
    address = models.CharField('Адресс', max_length=200)
    pin = models.CharField('ИНН', max_length=200)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name + self.decrypt()

    @staticmethod
    def encrypt(in_pin) -> str:
        in_pin = in_pin.encode('ascii')
        out_pin = base64.b64encode(in_pin)
        return out_pin.decode('ascii')

    def decrypt(self) -> str:
        pin = self.pin.encode('ascii')
        pin = base64.b64decode(pin)
        return pin.decode('ascii')

    decrypt.short_description = 'ИНН'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.pin = self.encrypt(self.pin)
        return super(MainUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)