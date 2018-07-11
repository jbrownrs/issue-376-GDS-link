# Generated by Django 2.0.7 on 2018-07-11 15:43

from django.db import migrations, models
import mediaplatform.models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplatform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.CharField(default=mediaplatform.models._make_token, editable=False, max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mediaitem',
            name='id',
            field=models.CharField(default=mediaplatform.models._make_token, editable=False, max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='permission',
            name='id',
            field=models.CharField(default=mediaplatform.models._make_token, editable=False, max_length=11, primary_key=True, serialize=False),
        ),
    ]
