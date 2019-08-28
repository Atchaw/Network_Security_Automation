import pprint

from django.shortcuts import render, get_object_or_404
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

from .models import Switch, Interface


def connect(self):
    devices = Switch.objects.all()
    print(devices)
    for device in devices:
        print("The hostname " + device.hostname)
        net_connect = ConnectHandler(device_type=device.device_type,
                                     ip=device.ip_vlan,
                                     username=device.username,
                                     password=device.password)
        output = net_connect.send_command("show interfaces | i (.* line protocol is )|(.* address is)",
                                          use_textfsm=True)

        pprint.pprint(output)
        for int in output:
            if "Vlan" not in int["interface"]:
                mode = net_connect.send_command(
                    "sh interfaces {0} switchport | i Operational Mode".format(int["interface"]), use_textfsm=True)
                print("The mode is  :" + mode.lower())

                if "access" in mode.lower():
                    interface = Interface(name_int=int["interface"],
                                          mac=int["address"],
                                          status=int["link_status"],
                                          mode="Access",
                                          device=device
                                          )
                else:
                    interface = Interface(name_int=int["interface"],
                                          mac=int["address"],
                                          status=int["link_status"],
                                          mode="Trunk",
                                          device=device
                                          )
                interface.save()
                print("savd")


def ssh_session(device):
    device_d = {'device_type': 'cisco_ios',
                'ip': device.ip_vlan,
                'username': device.username,
                'password': device.password}

    # SSH Iteration
    try:
        net_connect = ConnectHandler(**device_d)
        return net_connect
    except (AuthenticationException):
        print("Wrong Authentication >>> " + (device_d['ip']) + "\n")
        pass
    except (NetMikoTimeoutException):
        print("Timeout >>> " + (device_d['ip']) + "\n")
        pass
    except (EOFError):
        print("EOF Error >>> " + (device_d['ip']) + "\n")
        pass
    except (SSHException):
        print("Error SSH Exception >>> " + (device_d['ip']) + "\n")
        pass
    except Exception as unknown_error:
        print("Unkown Error >>> " + (device_d['ip']) + "\n")
        pass


def connectAll():
    connections = {}
    devices = Switch.objects.all()
    for device in devices:
        net_connect = ssh_session(device)
        connections[device.hostname] = net_connect
    return connections


connections = connectAll()


def device_get_interfaces(request, hostname):
    interfaces = Interface.objects.filter(device__hostname=hostname).order_by('name_int')
    device = get_object_or_404(Switch, hostname=hostname)
    return render(request, 'layer2/interfaces.html', {'interfaces': interfaces,
                                                      "device": device})


def device_list_view(request):
    devices = Switch.objects.all()
    interfaces = Interface.objects.all()
    return render(request, 'layer2/listDevices.html', {'devices': devices, "interfaces": interfaces})


def device_detail_view(request, hostname):
    device = get_object_or_404(Switch, hostname=hostname)
    return render(request, 'layer2/deviceDetail.html', {'device': device})


def port_security(request, host=None):
    print("----------------------------port security----------------------------")
    devices = Switch.objects.all()
    access_interfaces = Interface.objects.filter(device__hostname=host, mode="Access")
    net_connect = connections[str(host)]
    print("Connected")
    for int in access_interfaces:
        config_commands = [f"int {int}",
                           'switchport mode access',
                           'switchport port-security',
                           'switchport port-security maximum 10',
                           'switchport port-security violation shutdown',
                           'switchport port-security mac-address sticky']
        output = net_connect.send_config_set(config_commands)
        print(output)
    return render(request, "layer2/listDevices.html", {"devices": devices})


def dhcpSnooping(request):
    print("--------------------dhcpSnooping------------------------------")
    devices = Switch.objects.all()
    trunk_interfaces = Interface.objects.filter(mode="Trunk")
    print(trunk_interfaces)
    for net_connect in connections.values():
        for int in trunk_interfaces:
            config_commands = ['ip dhcp snooping',
                               f"int {int}",
                               'ip dhcp snooping trust',
                               ]
            output = net_connect.send_config_set(config_commands)
            print(output)
    return render(request, "layer2/listDevices.html", {"devices": devices})


def arppoising(request):
    print("--------------------Arp poising------------------------------")
    devices = Switch.objects.all()
    trunk_interfaces = Interface.objects.filter(mode="Trunk")
    for net_connect in connections.values():
        for int in trunk_interfaces:
            config_commands = ['ip dhcp snooping',
                               f"int {int}",
                               'ip dhcp snooping trust',
                               'ip arp inspection trust',
                               ]
            output = net_connect.send_config_set(config_commands)
            print(output)
    return render(request, "layer2/listDevices.html", {"devices": devices})


def stp(request):
    print("--------------------STP------------------------------")
    devices = Switch.objects.all()
    access_interfaces = Interface.objects.filter(mode="Access")
    interface = Interface.objects.all()
    for net_connect in connections.values():
        for int in access_interfaces:
            config_commands = [f"int {int}",
                               'spanning-tree portfast',
                               'spanning-tree bpduguard enable',
                               ]
            output = net_connect.send_config_set(config_commands)
            print(output)
        for int in interface:
            config_commands = [f"int {int}",
                               'spanning-tree guard root',
                               ]

            output = net_connect.send_config_set(config_commands)
            print(output)
    return render(request, "layer2/listDevices.html", {"devices": devices})
