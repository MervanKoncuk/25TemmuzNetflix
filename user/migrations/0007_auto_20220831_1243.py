# Generated by Django 3.2.12 on 2022-08-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_kullanici_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='resim',
            field=models.FileField(upload_to='kullanicilar/', verbose_name='Profil resmi'),
        ),
    ]
