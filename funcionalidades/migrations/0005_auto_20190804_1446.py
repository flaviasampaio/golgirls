# Generated by Django 2.2.3 on 2019-08-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionalidades', '0004_auto_20190804_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='senha',
            field=models.CharField(max_length=10, null=True, verbose_name='senha'),
        ),
    ]
