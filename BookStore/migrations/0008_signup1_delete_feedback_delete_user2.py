# Generated by Django 5.0.2 on 2024-04-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0007_alter_feedback_age_alter_feedback_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.DeleteModel(
            name='User2',
        ),
    ]