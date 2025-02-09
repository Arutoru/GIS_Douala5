# Generated by Django 4.2 on 2024-11-21 12:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site_touristique',
            fields=[
                ('id', models.IntegerField(primary_key='True', serialize=False)),
                ('arrondisse', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=20)),
                ('lieu_dit', models.CharField(max_length=20)),
                ('zone_trava', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='Site_toutristique',
        ),
    ]
