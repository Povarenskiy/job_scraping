# Generated by Django 4.2 on 2023-04-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0002_hhitems_last_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hhitems',
            name='number',
        ),
        migrations.AddField(
            model_name='hhitems',
            name='code',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Код вакансии'),
        ),
        migrations.AlterField(
            model_name='hhitems',
            name='exp',
            field=models.CharField(max_length=100, null=True, verbose_name='Опыт и режим работы'),
        ),
        migrations.AlterField(
            model_name='hhitems',
            name='last_update',
            field=models.DateTimeField(auto_created=True, verbose_name='Время последнего обновления'),
        ),
        migrations.AlterField(
            model_name='hhitems',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='Место работы'),
        ),
        migrations.AlterField(
            model_name='hhitems',
            name='salary',
            field=models.CharField(max_length=100, null=True, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='hhitems',
            name='title',
            field=models.CharField(max_length=250, null=True, verbose_name='Название вакансии'),
        ),
        migrations.AlterField(
            model_name='hhitems',
            name='url',
            field=models.CharField(max_length=250, null=True, verbose_name='Ссылка на вакансию'),
        ),
    ]
