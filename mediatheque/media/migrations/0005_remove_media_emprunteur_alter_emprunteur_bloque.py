# Generated by Django 5.1.2 on 2024-11-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_remove_emprunteur_auteur_emprunteur_bloque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='emprunteur',
        ),
        migrations.AlterField(
            model_name='emprunteur',
            name='bloque',
            field=models.BooleanField(default=True),
        ),
    ]
