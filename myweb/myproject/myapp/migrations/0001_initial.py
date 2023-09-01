# Generated by Django 4.2.4 on 2023-08-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('salary', models.BigIntegerField()),
            ],
        ),
    ]
