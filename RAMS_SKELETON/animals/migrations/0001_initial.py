# Generated by Django 2.1.7 on 2019-04-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(blank=True, choices=[('dog', 'Dog'), ('cat', 'Cat'), ('oth', 'Other')], max_length=50, null=True)),
                ('breed', models.CharField(blank=True, choices=[('val', 'Label')], max_length=50, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('pcolor', models.CharField(blank=True, choices=[('val', 'Label')], max_length=50, null=True)),
                ('scolor', models.CharField(blank=True, choices=[('val', 'Label')], max_length=50, null=True)),
                ('markings', models.CharField(blank=True, choices=[('val', 'Label')], max_length=50, null=True)),
                ('size', models.CharField(blank=True, choices=[('L', 'Large ()'), ('M', 'Medium ()'), ('S', 'Small ()')], max_length=1, null=True)),
                ('age', models.CharField(blank=True, choices=[('Y', 'Youth ()'), ('A', 'Adult ()'), ('E', 'Elderly ()')], max_length=1, null=True)),
                ('status', models.CharField(blank=True, choices=[('L', 'Large ()'), ('M', 'Medium ()'), ('S', 'Small ()')], max_length=3, null=True)),
                ('fixed', models.BooleanField(blank=True, null=True)),
                ('aggressive', models.BooleanField(blank=True, null=True)),
                ('confined', models.BooleanField(blank=True, null=True)),
                ('chipped', models.BooleanField(blank=True, null=True)),
                ('diet_needs', models.BooleanField(blank=True, null=True)),
                ('med_needs', models.BooleanField(blank=True, null=True)),
                ('collar_info', models.TextField(blank=True, null=True)),
                ('tag_info', models.TextField(blank=True, null=True)),
                ('chip_info', models.TextField(blank=True, null=True)),
                ('diet_notes', models.TextField(blank=True, null=True)),
                ('med_notes', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'ordering': [],
            },
        ),
    ]