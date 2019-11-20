# Generated by Django 2.1.4 on 2019-11-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockdatabase', '0002_auto_20191117_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_code', models.CharField(max_length=150, unique=True)),
                ('trade_date', models.CharField(max_length=100)),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('pre_close', models.FloatField()),
                ('change', models.FloatField()),
                ('pct_chg', models.FloatField()),
                ('vol', models.FloatField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]