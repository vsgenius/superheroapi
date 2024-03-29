# Generated by Django 4.0.5 on 2022-06-21 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearance',
            name='hero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appearance', to='api.hero'),
        ),
        migrations.AlterField(
            model_name='biography',
            name='hero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biography', to='api.hero'),
        ),
        migrations.AlterField(
            model_name='connections',
            name='hero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='api.hero'),
        ),
        migrations.AlterField(
            model_name='images',
            name='hero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.hero'),
        ),
        migrations.AlterField(
            model_name='powerstats',
            name='hero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='powerstats', to='api.hero'),
        ),
        migrations.AlterField(
            model_name='work',
            name='hero_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to='api.hero'),
        ),
    ]
