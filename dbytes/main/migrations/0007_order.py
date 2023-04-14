# Generated by Django 4.2 on 2023-04-13 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('ordertime', models.DateTimeField()),
                ('doneYN', models.CharField(max_length=1)),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
                ('mealID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meal')),
            ],
        ),
    ]
