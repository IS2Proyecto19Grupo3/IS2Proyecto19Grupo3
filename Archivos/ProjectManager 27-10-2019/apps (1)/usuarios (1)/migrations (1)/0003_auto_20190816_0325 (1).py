# Generated by Django 2.2.2 on 2019-08-16 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_auto_20190815_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios/imagenes'),
        ),
    ]