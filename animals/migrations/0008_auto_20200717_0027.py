# Generated by Django 3.0.8 on 2020-07-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0007_auto_20200515_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='attended_to',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='collared',
        ),
        migrations.AddField(
            model_name='animal',
            name='injured',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('yes', 'Yes'), ('no', 'No')], default='unknown', max_length=10),
        ),
    ]