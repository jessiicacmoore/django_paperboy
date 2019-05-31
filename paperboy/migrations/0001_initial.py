# Generated by Django 2.2.1 on 2019-05-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paperboy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experience', models.IntegerField(default=0)),
                ('earnings', models.PositiveIntegerField(default=0)),
                ('quota', models.PositiveIntegerField(default=50)),
            ],
        ),
    ]