# Generated by Django 4.0.2 on 2022-06-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_rename_cotizacion_cotizacion_coti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='annual',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='codeUyeda',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='coti',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='folio',
            field=models.IntegerField(unique=True),
        ),
    ]
