# Generated by Django 4.2.11 on 2024-04-19 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_management', '0004_schedule_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='verify',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hospital_management.hospital'),
        ),
    ]
