# Generated by Django 2.0.2 on 2018-02-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tovar', '0002_auto_20180214_1704'),
    ]

    operations = [
        migrations.RunSQL(
            sql = 'alter table tovar_tovar add column picture bytea ;',
            reverse_sql= 'alter table tovar_tovar drop column picture ;'
            ),
    ]