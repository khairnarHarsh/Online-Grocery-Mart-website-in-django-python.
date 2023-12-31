# Generated by Django 4.1.2 on 2023-03-22 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.BooleanField(default=False)),
                ('fullname', models.CharField(max_length=50)),
                ('mobile2', models.CharField(max_length=12)),
                ('pincode', models.CharField(max_length=8)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=10)),
                ('states', models.CharField(max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
