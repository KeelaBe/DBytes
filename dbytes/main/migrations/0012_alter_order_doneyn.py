# Generated by Django 4.2 on 2023-04-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_employeeid_order_employeename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='doneYN',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
