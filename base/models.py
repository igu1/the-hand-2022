from django.contrib.auth.models import User
from django.db import models


class Donation(models.Model):
    title = models.CharField(max_length=254)
    desc = models.TextField(max_length=2048, null=True)
    total = models.FloatField(default=0)
    money_need = models.FloatField(default=0)
    added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class DonatedPeople(models.Model):
    card = models.ForeignKey(Donation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " -> " + self.card.title


class DonationAutherization(models.Model):
    card = models.ForeignKey(Donation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ClientMessages(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name + " -> " + self.message[:25]
