# Generated by Django 5.1.1 on 2024-09-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('formation_date', models.DateField(blank=True, null=True)),
                ('members', models.ManyToManyField(blank=True, related_name='band_members', to='performer.artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='bands',
            field=models.ManyToManyField(blank=True, null=True, related_name='artists', to='performer.band'),
        ),
    ]
