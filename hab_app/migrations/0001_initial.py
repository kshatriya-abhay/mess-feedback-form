# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllHostelMetaData',
            fields=[
                ('hostelName', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('hostelCode', models.CharField(max_length=255, unique=True)),
                ('hostelGensec', models.CharField(max_length=255)),
                ('hostelCTid', models.CharField(max_length=255, unique=True)),
                ('hostelRoom', models.CharField(max_length=255, unique=True)),
                ('hostelRoomOccupant', models.CharField(max_length=255, unique=True)),
                ('hostelViewPermission', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'AllHostelMetaData',
                'verbose_name_plural': 'AllHostelMetaData',
            },
        ),
        migrations.CreateModel(
            name='HostelRoom',
            fields=[
                ('roomNo', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('roomOccupancyType', models.CharField(max_length=255)),
                ('floorInfo', models.CharField(max_length=255)),
                ('roomStatus', models.CharField(max_length=255)),
                ('roomOccupancyGender', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'HostelRoom',
                'verbose_name_plural': 'HostelRoom',
            },
        ),
        migrations.CreateModel(
            name='HostelRoomOccupantRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelName', models.CharField(max_length=255)),
                ('roomNo', models.CharField(max_length=255)),
                ('occupantId', models.CharField(max_length=255)),
                ('messStatus', models.CharField(max_length=255)),
                ('toMess', models.DateField()),
                ('fromMess', models.DateField()),
                ('toRoomStay', models.DateField()),
                ('fromRoomStay', models.DateField()),
                ('comment', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'HostelRoomOccupantRelation',
                'verbose_name_plural': 'HostelRoomOccupantRelation',
            },
        ),
        migrations.CreateModel(
            name='HostelViewAccess',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('webmail', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'HostelViewAccess',
                'verbose_name_plural': 'HostelViewAccess',
            },
        ),
        migrations.CreateModel(
            name='OccupantCategory',
            fields=[
                ('occupantId', models.IntegerField()),
                ('abbrevation', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'OccupantCategory',
                'verbose_name_plural': 'OccupantCategory',
            },
        ),
        migrations.CreateModel(
            name='OccupantDetails',
            fields=[
                ('idType', models.CharField(max_length=255)),
                ('idNo', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=255)),
                ('saORda', models.CharField(max_length=255)),
                ('webmail', models.CharField(max_length=255)),
                ('altEmail', models.CharField(max_length=255)),
                ('mobNo', models.CharField(max_length=255)),
                ('emgercencyNo', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('bankAccount', models.CharField(max_length=255)),
                ('IFSCCode', models.CharField(max_length=255)),
                ('accHolderName', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'OccupantDetails',
                'verbose_name_plural': 'OccupantDetails',
            },
        ),
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('roomId', models.IntegerField()),
                ('abbrevation', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'RoomCategory',
                'verbose_name_plural': 'RoomCategory',
            },
        ),
        migrations.CreateModel(
            name='barakRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='barakRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='barakView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='bramhaputraRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='bramhaputraRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='bramhaputraView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='dhansiriRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='dhansiriRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='dhansiriView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='dibangRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='dibangRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='dibangView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='dihingRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='dihingRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='dihingView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='kamengRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='kamengRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='kamengView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='kapiliRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='kapiliRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='kapiliView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='lohitRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='lohitRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='lohitView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='manasRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='manasRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='manasView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='marriedScholarRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='marriedScholarRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='marriedScholarView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='siangRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='siangRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='siangView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='subansiriRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='subansiriRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='subansiriView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
        migrations.CreateModel(
            name='umiamRoom',
            fields=[
                ('hostelroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoom')),
            ],
            bases=('hab_app.hostelroom',),
        ),
        migrations.CreateModel(
            name='umiamRORelation',
            fields=[
                ('hostelroomoccupantrelation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelRoomOccupantRelation')),
            ],
            bases=('hab_app.hostelroomoccupantrelation',),
        ),
        migrations.CreateModel(
            name='umiamView',
            fields=[
                ('hostelviewaccess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hab_app.HostelViewAccess')),
            ],
            bases=('hab_app.hostelviewaccess',),
        ),
    ]
