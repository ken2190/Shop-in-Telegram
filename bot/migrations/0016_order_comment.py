# Generated by Django 3.2.6 on 2021-08-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_order_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default='', null=True, verbose_name='Комментарий для пользователя'),
        ),
    ]