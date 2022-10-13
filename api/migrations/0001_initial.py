# Generated by Django 4.0.5 on 2022-10-13 17:09

import api.models.booking
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('account_type', models.IntegerField(choices=[(-1, 'ERROR'), (0, 'DEFAULT'), (1, 'SHIPPER'), (2, 'BROKER'), (3, 'WAREHOUSE'), (4, 'CARRIER'), (5, 'PORTOPS')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.CharField(default='', max_length=12)),
                ('unloading_destination_address', models.CharField(default='', max_length=80)),
                ('loading_origin_address', models.CharField(default='', max_length=80)),
                ('pickup_address', models.CharField(default='', max_length=80)),
                ('pickup_appt', models.DateTimeField(default=api.models.booking._pickup_appt)),
                ('rail_cutoff', models.DateTimeField(blank=True, null=True)),
                ('port_cutoff', models.DateTimeField(default=api.models.booking._port_cut)),
                ('delivery_address', models.CharField(default='', max_length=80)),
                ('delivery_appt', models.DateTimeField(default=api.models.booking._delivery_appt)),
                ('booking_status', models.IntegerField(choices=[(4, 'ERROR'), (0, ''), (1, 'PENDING'), (2, 'COMPLETE'), (3, 'CLOSED')], default=0)),
                ('are_documents_ready', models.BooleanField(default=False)),
                ('are_dues_paid', models.BooleanField(default=False)),
                ('has_issue', models.BooleanField(default=False)),
                ('booking_notes', models.TextField(blank=True, default='')),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_bookings', to='api.appuser')),
                ('carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrier_bookings', to='api.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container', models.CharField(max_length=8)),
                ('equipment_type', models.IntegerField(choices=[(0, ''), (1, '40OG'), (2, '20ST'), (3, '40ST'), (4, '20HC'), (5, '40HC')], default=0)),
                ('equipment_location', models.IntegerField(choices=[(6, 'YARD'), (7, 'RAIL'), (8, 'SAIL'), (9, 'PORT'), (10, 'BERTH'), (11, 'PICKUP'), (12, 'TRANSIT'), (13, 'STORAGE'), (14, 'DELIVERY'), (15, 'WAREHOUSE'), (16, 'INSPECTION')], default=6)),
                ('is_needs_inspection', models.BooleanField(default=False)),
                ('is_overweight', models.BooleanField(default=False)),
                ('is_container_damaged', models.BooleanField(default=False)),
                ('is_in_use', models.BooleanField(default=False)),
                ('container_notes', models.TextField(blank=True, default='')),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='containers', to='api.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voyage', models.CharField(max_length=10)),
                ('service', models.IntegerField(choices=[(0, ''), (1, 'WC'), (2, 'EC'), (3, 'NE'), (4, 'SE'), (5, 'GU')], default=0)),
                ('vessel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voyages', to='api.vessel')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('is_product_damaged', models.BooleanField(default=False)),
                ('is_fragile', models.BooleanField(default=False)),
                ('is_reefer', models.BooleanField(default=False)),
                ('is_haz', models.BooleanField(default=False)),
                ('booking_notes', models.TextField(blank=True, default='')),
                ('container', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='api.container')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='loading_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loading_port_bookings', to='api.port'),
        ),
        migrations.AddField(
            model_name='booking',
            name='unloading_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unloading_port_bookings', to='api.port'),
        ),
        migrations.AddField(
            model_name='booking',
            name='voyage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voyage_bookings', to='api.voyage'),
        ),
    ]
