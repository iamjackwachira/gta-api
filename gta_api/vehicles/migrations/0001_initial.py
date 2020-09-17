# Generated by Django 3.1.1 on 2020-09-17 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealLifeVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleStorageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleWorkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70, unique=True)),
                ('vehicle_class', models.CharField(max_length=70, verbose_name=(('boats', 'Boats'), ('commercial', 'Commercial'), ('compacts', 'Compacts'), ('coupes', 'Coupes'), ('cycles', 'Cycles'), ('emergency', 'Emergency'), ('helicopters', 'Helicopters'), ('industrial', 'Industrial'), ('military', 'Military'), ('motorcycles', 'Motorcycles'), ('muscle', 'Muscle'), ('offroad', 'Off-road'), ('openwheel', 'Open-wheel'), ('planes', 'Planes'), ('sedan', 'Sedan'), ('service', 'Service'), ('sports', 'Sports'), ('sport_classic', 'Sport Classic'), ('super', 'Super'), ('suv', 'SUV'), ('utility', 'Utility'), ('vans', 'Vans')))),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sell_ability', models.CharField(blank=True, choices=[('purchased_high_end', 'Purchased High End'), ('purchased_or_stolen', 'Purchased Or Stolen'), ('only_stolen', 'Only Stolen'), ('not_sellable', 'Can not Be Sold')], help_text='If the vehicle can be sold', max_length=50, null=True)),
                ('stolen_sell_value', models.DecimalField(decimal_places=2, help_text='Max sell value if stolen', max_digits=20)),
                ('resale_value', models.DecimalField(decimal_places=2, help_text='Max sell value if purchased', max_digits=20)),
                ('top_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight_in_kg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('drive_train', models.CharField(choices=[('fwd', 'FWD'), ('rwd', 'RWD'), ('awd', 'AWD'), ('4wd', '4WD')], max_length=3)),
                ('num_gears', models.PositiveSmallIntegerField()),
                ('num_doors', models.PositiveSmallIntegerField()),
                ('speed_rating', models.PositiveSmallIntegerField()),
                ('acceleration_rating', models.PositiveSmallIntegerField()),
                ('handling_rating', models.PositiveSmallIntegerField()),
                ('braking_rating', models.PositiveSmallIntegerField()),
                ('based_on', models.ForeignKey(blank=True, help_text="Real life vehicle that it's based on", null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.reallifevehicle')),
                ('game_edition', models.ManyToManyField(to='core.GameEdition')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehiclemanufacturer')),
                ('storage_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehiclestoragelocation')),
                ('workshop', models.ForeignKey(help_text='Workshop for modifying vehicle', on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicleworkshop')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
                'ordering': ['-created_on'],
            },
        ),
    ]
