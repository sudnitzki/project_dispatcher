# Generated by Django 4.0.5 on 2022-07-06 16:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
            ],
            options={
                'ordering': ['country', 'brand'],
            },
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the Type of the trailer (e.g. Refrigerated Trailers)', max_length=200, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=6, verbose_name='Plate number')),
                ('summary', models.TextField(help_text='Trumpas knygos aprašymas', max_length=1000, verbose_name='Summary')),
                ('vin', models.CharField(help_text='17 characters <a href="https://www.autocheck.com/vehiclehistory/vin-basics', max_length=17, verbose_name='Vin code')),
                ('producer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dispatcher.producer')),
                ('trailer', models.ManyToManyField(help_text='Select the Type of the trailer', to='dispatcher.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TruckInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Dispatchers ID for the Truck', primary_key=True, serialize=False)),
                ('expected_return', models.DateField(blank=True, null=True, verbose_name='Will be available')),
                ('status', models.CharField(blank=True, choices=[('ser', 'Service'), ('tri', 'Trip'), ('rea', 'Ready'), ('res', 'Reserved')], default='s', help_text='Status', max_length=3)),
                ('truck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dispatcher.truck')),
            ],
            options={
                'ordering': ['expected_return'],
            },
        ),
    ]