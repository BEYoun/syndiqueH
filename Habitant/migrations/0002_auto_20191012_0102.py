# Generated by Django 2.2.3 on 2019-10-11 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Habitant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
