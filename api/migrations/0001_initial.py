# Generated by Django 3.2.4 on 2021-06-16 20:39

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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BkgStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CntrStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container', models.CharField(max_length=50)),
                ('equipment_size', models.CharField(max_length=7)),
                ('is_damaged', models.BooleanField()),
                ('is_need_inspection', models.BooleanField()),
                ('is_overweight', models.BooleanField()),
                ('is_in_use', models.BooleanField()),
                ('notes', models.TextField(blank=True, default='')),
                ('container_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.cntrstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('are_docs_ready', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Due',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('are_dues_paid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voyage', models.CharField(max_length=10)),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.vessel')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('is_fragile', models.BooleanField()),
                ('is_haz', models.BooleanField()),
                ('is_damaged', models.BooleanField()),
                ('is_reefer', models.BooleanField()),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.container')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.CharField(max_length=50)),
                ('loading_origin', models.CharField(max_length=50)),
                ('unloading_destination', models.CharField(max_length=50)),
                ('pickup_appt', models.DateTimeField()),
                ('port_cutoff', models.DateTimeField()),
                ('rail_cutoff', models.DateTimeField(blank=True, null=True)),
                ('has_issue', models.BooleanField()),
                ('notes', models.TextField(blank=True, default='')),
                ('booking_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.bkgstatus')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.container')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.document')),
                ('due', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.due')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.port')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.appuser')),
                ('voyage_reference', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.voyage')),
            ],
        ),
    ]
