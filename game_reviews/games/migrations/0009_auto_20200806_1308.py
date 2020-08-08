# Generated by Django 3.1 on 2020-08-06 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20200806_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(to='games.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.tagcategory'),
        ),
    ]