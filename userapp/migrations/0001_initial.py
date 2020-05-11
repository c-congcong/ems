# Generated by Django 2.0.6 on 2020-04-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('z_name', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=30)),
                ('sex', models.BooleanField()),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pic', models.ImageField(upload_to='img')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
