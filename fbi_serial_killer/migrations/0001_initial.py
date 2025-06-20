# Generated by Django 5.2 on 2025-06-20 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FBI_Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='探員姓名')),
                ('badge_number', models.CharField(max_length=10, unique=True, verbose_name='徽章編號')),
                ('join_year', models.IntegerField(verbose_name='入職年份')),
                ('specialization', models.CharField(blank=True, max_length=100, verbose_name='專長領域')),
            ],
            options={
                'verbose_name': 'FBI探員',
                'verbose_name_plural': 'FBI探員',
            },
        ),
        migrations.CreateModel(
            name='Serial_Killer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('alias', models.CharField(blank=True, max_length=100, verbose_name='別名')),
                ('crime_period_start', models.IntegerField(verbose_name='犯罪開始年份')),
                ('crime_period_end', models.IntegerField(verbose_name='犯罪結束年份')),
                ('victim_count', models.IntegerField(verbose_name='受害人數量')),
                ('description', models.TextField(blank=True, verbose_name='犯罪描述')),
            ],
            options={
                'verbose_name': '連環殺手',
                'verbose_name_plural': '連環殺手',
            },
        ),
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capture_date', models.DateField(verbose_name='捉拿日期')),
                ('location', models.CharField(max_length=200, verbose_name='捉拿地點')),
                ('details', models.TextField(blank=True, verbose_name='捉拿詳情')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbi_serial_killer.fbi_agent', verbose_name='負責探員')),
                ('serial_killer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbi_serial_killer.serial_killer', verbose_name='連環殺手')),
            ],
            options={
                'verbose_name': '捉拿記錄',
                'verbose_name_plural': '捉拿記錄',
            },
        ),
    ]
