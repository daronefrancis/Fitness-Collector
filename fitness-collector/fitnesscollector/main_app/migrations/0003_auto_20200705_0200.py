# Generated by Django 3.0.6 on 2020-07-05 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(verbose_name='workout date'),
        ),
        migrations.AddField(
            model_name='workout',
            name='equipment',
            field=models.ManyToManyField(to='main_app.Equipment'),
        ),
    ]
