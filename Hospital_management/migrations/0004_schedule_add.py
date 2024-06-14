# Generated by Django 4.2.11 on 2024-04-19 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_management', '0003_complaints_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Hospital_management.hospital')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Hospital_management.vaccin')),
            ],
        ),
    ]
