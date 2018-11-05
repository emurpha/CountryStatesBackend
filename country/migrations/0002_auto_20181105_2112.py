# Generated by Django 2.1.2 on 2018-11-05 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='state',
            name='country_id',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_code',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_name',
        ),
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AddField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AddField(
            model_name='state',
            name='countryId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='country.Country'),
        ),
        migrations.AddField(
            model_name='state',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
