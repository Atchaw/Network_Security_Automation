# Generated by Django 2.0.13 on 2019-07-17 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('hostname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('device_type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_int', models.CharField(max_length=20)),
                ('mac', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('UP', 'UP'), ('DOWN', 'DOWN')], max_length=5)),
                ('mode', models.CharField(choices=[('Access', 'Access'), ('Trunk', 'Trunk')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layer2.Device')),
                ('ip_vlan', models.GenericIPAddressField(protocol='IPv4')),
            ],
            bases=('layer2.device',),
        ),
        migrations.AddField(
            model_name='interface',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layer2.Device'),
        ),
    ]
