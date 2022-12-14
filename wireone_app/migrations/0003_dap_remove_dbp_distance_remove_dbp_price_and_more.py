# Generated by Django 4.1.1 on 2022-10-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wireone_app', '0002_alter_tmf_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='dbp',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='dbp',
            name='price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='dap',
        ),
        migrations.RemoveField(
            model_name='tmf',
            name='Time',
        ),
        migrations.RemoveField(
            model_name='tmf',
            name='price',
        ),
        migrations.AddField(
            model_name='dbp',
            name='data',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dbp',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tmf',
            name='data',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmf',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
