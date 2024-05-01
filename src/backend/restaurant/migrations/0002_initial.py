# Generated by Django 4.0.3 on 2022-03-15 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='rid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='rid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='rid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
