# Generated by Django 3.1.7 on 2021-04-08 06:54

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
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=50)),
                ('borrower_id', models.IntegerField()),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('major', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_time', models.DateTimeField()),
                ('borrower_id', models.IntegerField()),
                ('lender_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('img', models.ImageField(upload_to='images')),
                ('borrower_confirm', models.BooleanField(default=False)),
                ('lender_confirm', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TransferRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=30)),
                ('request_time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]