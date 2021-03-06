# Generated by Django 3.2.4 on 2021-06-15 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг продукта')),
                ('title', models.CharField(max_length=150, verbose_name='Название продукта')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.FloatField(default=0, verbose_name='Цена продукта')),
                ('discount', models.FloatField(verbose_name='Скидка')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce_shop.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
