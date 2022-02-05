# Generated by Django 3.2.6 on 2021-08-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_file_order_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='kol_ask',
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Комментарий для пользователя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='step',
            field=models.IntegerField(choices=[(1, 'Клиент вводит данные'), (2, 'Не оплачен'), (3, 'Оплачен'), (4, 'Отправлен поставщику'), (5, 'Готов'), (6, 'Отменен'), (7, 'Отказ оператора')], verbose_name='Статус заказа'),
        ),
    ]
