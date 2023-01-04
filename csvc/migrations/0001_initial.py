# Generated by Django 4.0.4 on 2022-05-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csvc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=10)),
                ('name', models.TextField(max_length=255)),
                ('den', models.IntegerField(default=25)),
                ('ban_ghe', models.IntegerField(default=25)),
                ('may_chieu', models.IntegerField(default=25)),
                ('quat', models.IntegerField(default=25)),
                ('dieu_hoa', models.IntegerField(default=25)),
            ],
        ),
    ]
