# Generated by Django 4.1.2 on 2023-03-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
