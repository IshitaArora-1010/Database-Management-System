# Generated by Django 2.2.10 on 2021-05-19 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210519_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement_skill',
            name='participant_id_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.participant_skill'),
        ),
    ]
