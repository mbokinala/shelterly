# Generated by Django 3.0.4 on 2020-05-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0004_auto_20200427_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='apartment',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='directions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='outcome',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='owner_notification_notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='zip_code',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('VA', 'VA'), ('VT', 'VT'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')], default='', max_length=2),
            preserve_default=False,
        ),
    ]