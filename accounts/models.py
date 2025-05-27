from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Account(models.Model):
    class AccountType(models.TextChoices):
        SAVINGS = 'savings', 'Savings'
        INVESTMENT = 'investment', 'Investment'

    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="accounts")
    account_type = models.CharField(
        max_length=25,
        choices=AccountType.choices,
        default=AccountType.SAVINGS
    )
    balance = models.BigIntegerField()

    def __str__(self):
        return f"{self.account_type} - {self.client.name}"
