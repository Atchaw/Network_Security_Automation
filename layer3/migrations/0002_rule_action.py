# Generated by Django 2.0.13 on 2019-07-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layer3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='action',
            field=models.CharField(choices=[('permit', 'permit'), ('deny', 'deny')], default=2, max_length=10),
            preserve_default=False,
        ),
    ]
