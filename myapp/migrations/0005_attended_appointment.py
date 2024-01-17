# Generated by Django 4.2.7 on 2024-01-08 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_appointment_appointment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attended_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_dignosed', models.CharField(max_length=100)),
                ('prescription', models.CharField(max_length=100)),
                ('follow_up_date', models.CharField(max_length=100)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.appointment')),
            ],
        ),
    ]