# Generated by Django 4.1 on 2022-09-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_watchlists_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlists',
            name='watched',
            field=models.TextField(),
        ),
    ]