# Generated by Django 3.2.12 on 2023-02-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('positionx', models.IntegerField()),
                ('positiony', models.IntegerField()),
            ],
        ),
    ]