# Generated by Django 5.1.7 on 2025-03-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abhay', '0006_alter_contact_whathapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='whathapp',
            field=models.TextField(max_length=30),
        ),
    ]
