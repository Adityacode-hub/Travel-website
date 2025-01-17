# Generated by Django 4.2.4 on 2024-04-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122, unique=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
