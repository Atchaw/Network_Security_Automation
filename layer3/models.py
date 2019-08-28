from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from layer2.models import Device


class Rule(models.Model):
    PROTOCOL = (
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
        ('ICMP', 'ICMP')
    )
    ACTIONS = (
        ('permit', 'permit'),
        ('deny', 'deny'),
    )
    number = models.IntegerField(null=False, unique=True,
                                 validators=[MinValueValidator(100), MaxValueValidator(199)])
    sourceIP = models.GenericIPAddressField(protocol='IPv4')
    destinationIP = models.GenericIPAddressField(protocol='IPv4')
    protocol = models.CharField(max_length=6, choices=PROTOCOL)
    action = models.CharField(max_length=10, choices=ACTIONS)

    def __str__(self):
        return str(self.number)


class Router(Device):
    # ID
    ip_loopback = models.GenericIPAddressField(protocol='IPv4')
    rules = models.ManyToManyField(
        Rule,
        related_name='rules'
    )

    def __str__(self):
        return str(self.ip_loopback)


class InterfaceRouter(models.Model):

    Status = (
        ('UP', 'UP'),
        ('DOWN', 'DOWN'),
    )
    # ID
    name_int = models.CharField(max_length=20)
    mac = models.CharField(max_length=100)
    # Status: Up/Down
    status = models.CharField(max_length=5, choices=Status)

    device = models.ForeignKey(Router, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name_int)