# Generated by Django 4.0.2 on 2022-05-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_cotizacion_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='quote',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='quotation',
            field=models.PositiveSmallIntegerField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='adhesive',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='annual',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='axis',
            field=models.FloatField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='backup',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='codeUyeda',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='customerCode',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='customers',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='delivery',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='development',
            field=models.FloatField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='finished',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='folio',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink1',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink10',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink2',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink3',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink4',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink5',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink6',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink7',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink8',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='ink9',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='inkAdhesive',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='inkBackup',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='inkFront',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='letterColor',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='output',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='packaging',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='place',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='press',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='price',
            field=models.FloatField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prodpackaging',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='request',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='specialty',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='speed',
            field=models.PositiveSmallIntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='suaje',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='substrate',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='test',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='typeCo',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='typeDelivery',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='typeInk',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='variant',
            field=models.CharField(max_length=50),
        ),
    ]
