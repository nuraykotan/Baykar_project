# Generated by Django 4.2.18 on 2025-02-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0004_personnel_rol_alter_personnel_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='rol',
            field=models.CharField(choices=[('admin', 'Admin'), ('developer', 'Developer'), ('manager', 'Manager')], default='developer', max_length=100),
        ),
    ]
