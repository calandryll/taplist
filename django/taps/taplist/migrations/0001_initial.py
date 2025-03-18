# Generated by Django 3.2.5 on 2022-02-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brew_name', models.TextField()),
                ('style', models.TextField(max_length=255, null=True)),
                ('OG', models.FloatField(null=True)),
                ('FG', models.FloatField(null=True)),
                ('date_brewed', models.DateField(null=True)),
                ('SRM', models.FloatField(null=True)),
                ('IBU', models.FloatField(null=True)),
                ('ABV', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('tasting_notes', models.TextField(null=True)),
                ('tap', models.CharField(choices=[('1', 'Tap 1'), ('2', 'Tap 2'), ('3', 'Tap 3')], max_length=1, null=True)),
                ('kegged', models.BooleanField(default=False)),
                ('empty', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['tap'],
            },
        ),
        migrations.CreateModel(
            name='srmRGB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srm', models.CharField(max_length=3)),
                ('R', models.CharField(max_length=3)),
                ('G', models.CharField(max_length=3)),
                ('B', models.CharField(max_length=3)),
            ],
        ),
    ]
