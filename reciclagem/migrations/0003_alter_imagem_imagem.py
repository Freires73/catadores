# Generated by Django 5.0.6 on 2024-05-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciclagem', '0002_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(upload_to='imagem_produto'),
        ),
    ]
