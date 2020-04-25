# Generated by Django 3.0.5 on 2020-04-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.IntegerField(blank=True, default=134112323),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='codeUTEC',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nTokens',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
