# Generated by Django 4.0.5 on 2022-07-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_cityinfo_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityinfo',
            name='url',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]