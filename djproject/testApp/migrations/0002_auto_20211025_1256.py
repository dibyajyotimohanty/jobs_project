# Generated by Django 3.2.8 on 2021-10-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='punejobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Company', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Eligibility', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phonenumber', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='chennaijobs',
            name='Phonenumbe',
        ),
        migrations.AddField(
            model_name='chennaijobs',
            name='Phonenumber',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
