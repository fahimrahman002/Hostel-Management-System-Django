# Generated by Django 3.2.12 on 2022-04-01 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_bazardetail_mealrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealrecord',
            name='hostel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.hostel'),
            preserve_default=False,
        ),
    ]
