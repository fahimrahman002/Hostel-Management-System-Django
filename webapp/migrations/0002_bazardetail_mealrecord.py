# Generated by Django 3.2.12 on 2022-04-01 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('meal_lunch', models.BooleanField(default=True)),
                ('meal_dinner', models.BooleanField(default=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='BazarDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('details', models.TextField(blank=True, default='', null=True)),
                ('expense', models.IntegerField(default=0)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.hostel')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.member')),
            ],
        ),
    ]