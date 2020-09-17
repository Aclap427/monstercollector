# Generated by Django 3.1.1 on 2020-09-17 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_monster_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='image',
            field=models.ImageField(height_field=50, null=True, upload_to='main_app/static/images', width_field=50),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('TIMEFRAME', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], default='Afternoon', max_length=1)),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.monster')),
            ],
        ),
    ]