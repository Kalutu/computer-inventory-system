# Generated by Django 4.2.5 on 2023-09-20 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_computer_export_to_csv'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(blank=True, max_length=30, null=True)),
                ('IP_address', models.CharField(blank=True, max_length=30, null=True)),
                ('MAC_address', models.CharField(blank=True, max_length=30, null=True)),
                ('users_name', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase Date(mm/dd/2019)')),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('operating_system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangoapp.operating_system')),
            ],
        ),
    ]
