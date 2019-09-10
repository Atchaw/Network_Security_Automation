from django.db import models
from django.urls import reverse


class Device(models.Model):
    username = models.CharField(max_length=30)
    hostname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    device_type = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Switch(Device):
    # ID
    ip_vlan = models.GenericIPAddressField(protocol='IPv4')

    def __str__(self):
        return str(self.ip_vlan)

    def get_absolute_url(self):
        return reverse('device_list_view:detail', args=[self.ip_vlan])


class Interface(models.Model):
    Mode = (
        ('Access', 'Access'),
        ('Trunk', 'Trunk'),
    )
    Status = (
        ('UP', 'UP'),
        ('DOWN', 'DOWN'),
    )
    # ID
    name_int = models.CharField(max_length=20)
    mac = models.CharField(max_length=100)
    # Status: Up/Down
    status = models.CharField(max_length=5, choices=Status)
    # Mode Access/Trunk
    mode = models.CharField(max_length=10, choices=Mode)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name_int)
