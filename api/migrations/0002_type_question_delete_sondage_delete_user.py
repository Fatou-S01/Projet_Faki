# Generated by Django 4.0.3 on 2022-06-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='sondage',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
