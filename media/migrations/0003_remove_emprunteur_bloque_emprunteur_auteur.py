# Generated by Django 5.1.2 on 2024-10-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_alter_media_date_emprunt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprunteur',
            name='bloque',
        ),
        migrations.AddField(
            model_name='emprunteur',
            name='auteur',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
    ]
