# Generated by Django 2.1.11 on 2019-11-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='cage',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='shelter',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cage',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/shelter'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
