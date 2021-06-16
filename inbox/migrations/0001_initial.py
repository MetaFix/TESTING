# Generated by Django 3.2.4 on 2021-06-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='Имя клиента')),
                ('last_name', models.CharField(max_length=250, verbose_name='Фамилия клиента')),
                ('email', models.EmailField(max_length=250, verbose_name='Email клиента')),
                ('phone', models.EmailField(max_length=250, verbose_name='Номер телефона клиента')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
