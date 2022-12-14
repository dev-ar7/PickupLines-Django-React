# Generated by Django 4.0.6 on 2022-07-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PickupLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=500)),
                ('cat', models.CharField(choices=[('BEST', 'Best'), ('CUTE', 'Cute'), ('FUNNY', 'Funny'), ('ROMANTIC', 'Romantic')], max_length=8)),
                ('tag', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
