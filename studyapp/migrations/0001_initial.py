# Generated by Django 3.1.4 on 2021-02-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('regid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('pcode', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
                ('role', models.CharField(max_length=50)),
                ('dt', models.CharField(max_length=200)),
            ],
        ),
    ]
