from django.db import models


class Organization(models.Model):
    fullname = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    inn = models.CharField(max_length=12)
    kpp = models.CharField(max_length=9, blank=True)
    off_address = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '<Organization {}>'.format(self.name)


class Contract(models.Model):
    # fullname = models.CharField(max_length=128)  # предмет контракта
    name = models.CharField(max_length=64, null=True)  # предмет контракта кратко
    date = models.DateField(null=True)  # дата договора
    number = models.CharField(max_length=32, null=True)  # номер договора
    price = models.FloatField(null=True)  # цена договора
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)  # контрагент
    we_supplier = models.BooleanField()  # True если мы поставщик, False если мы покупатель
    # startdate = models.DateField()
    # enddate = models.DateField()

    def __str__(self):
        return '<Contract № {}>'.format(self.number)


