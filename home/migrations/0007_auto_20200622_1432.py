# Generated by Django 3.0.7 on 2020-06-22 13:32

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200622_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=100, null=True),
        ),
    ]