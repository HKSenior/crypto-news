from django.db import models


class Coin(models.Model):
    imageUrl = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, unique=True)
    algorithm = models.CharField(max_length=50)
    proofType = models.CharField(max_length=50)
    totalCoinSupply = models.DecimalField(max_digits=32, decimal_places=2)
    isTrading = models.BooleanField(default=False)
    totalCoinsMined = models.DecimalField(max_digits=40, decimal_places=8)
    blockNumber = models.IntegerField(default=-1)
    netHashesPerSecond = models.DecimalField(max_digits=40, decimal_places=8)
    blockReward = models.DecimalField(max_digits=32, decimal_places=16)
    blockTime = models.IntegerField(default=-1)
