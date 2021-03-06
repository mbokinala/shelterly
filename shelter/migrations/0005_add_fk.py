# Generated by Django 3.0.8 on 2020-08-08 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0004_removing_nulls'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='shelter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shelter.Shelter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/shelter'),
        ),
    ]
