# Generated by Django 3.1 on 2020-08-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_review_max_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='max_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
