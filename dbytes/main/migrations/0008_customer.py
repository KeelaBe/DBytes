# Generated by Django 4.2 on 2023-04-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=50)),
            ],
        ),
    ]