# Generated by Django 3.1.7 on 2021-04-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=30)),
                ('is_book_valid', models.BooleanField(default=False)),
                ('book_id', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=50)),
                ('valid_date', models.DateField(null=True)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
