# Generated by Django 2.2.3 on 2019-08-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionalidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='senha',
            field=models.CharField(default='', max_length=255, verbose_name='Senha'),
            preserve_default=False,
        ),
    ]
