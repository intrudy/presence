# Generated by Django 5.0.4 on 2024-05-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_alter_cohort_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort',
            name='name',
            field=models.CharField(default='9b604fec-0f9e-4bb1-b78a-b8d057791e00', max_length=128),
        ),
    ]