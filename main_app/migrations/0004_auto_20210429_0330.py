# Generated by Django 3.2 on 2021-04-29 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_joke_joke'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='appproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='joke',
            name='category',
            field=models.CharField(choices=[('R', 'Random Jokes'), ('Y', 'Yo Mama Jokes'), ('D', 'Dad Puns'), ('K', 'Knock Knock Jokes'), ('B', 'Bar Jokes'), ('C', 'Computer Jokes'), ('S', 'Sports Jokes'), ('D', 'Dog Jokes')], default='R', max_length=50),
        ),
    ]
