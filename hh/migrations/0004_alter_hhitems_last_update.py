# Generated by Django 4.2 on 2023-04-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0003_remove_hhitems_number_hhitems_code_alter_hhitems_exp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hhitems',
            name='last_update',
            field=models.DateTimeField(auto_created=True, null=True, verbose_name='Время последнего обновления'),
        ),
    ]
