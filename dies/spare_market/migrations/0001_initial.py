# Generated by Django 3.1.4 on 2020-12-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(max_length=50)),
                ('part_number', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Records',
            },
        ),
    ]
