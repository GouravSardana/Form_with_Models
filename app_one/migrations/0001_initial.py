# Generated by Django 2.1.1 on 2018-10-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('roll_no', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
