# Generated by Django 2.2.2 on 2019-06-07 16:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('parking_mode', models.CharField(choices=[('hour', 'Hour'), ('day', 'Day')], default='hour', help_text='Decides if slot is available or booked', max_length=11)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('booked', 'booked'), ('reserved', 'reserved')], default='available', help_text='Decides if slot is availaible or booked', max_length=11)),
                ('day', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'slots',
            },
        ),
    ]
