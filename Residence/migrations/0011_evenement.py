# Generated by Django 2.2.3 on 2019-10-26 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20191010_2310'),
        ('Residence', '0010_auto_20191025_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(max_length=200)),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='evenement')),
                ('batiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Batiment')),
            ],
        ),
    ]
