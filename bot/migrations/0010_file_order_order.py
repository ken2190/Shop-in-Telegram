# Generated by Django 3.2.6 on 2021-08-16 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_product_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_order', models.FileField(null=True, upload_to='', verbose_name='Загружаемые данные')),
            ],
            options={
                'verbose_name': 'Файлы',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField(choices=[(1, 'Клиент обрабатывает'), (2, 'Клиент не оплатил'), (3, 'Обрабатывается менеджером'), (4, 'Успешно доставлено'), (5, 'Отменен')], verbose_name='Статус заказа')),
                ('data_have', models.TextField(null=True, verbose_name='Введенные данные пользователем')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.profile')),
            ],
            options={
                'verbose_name': 'Заявка на покупку',
                'verbose_name_plural': 'Заявки на покупку',
            },
        ),
    ]
