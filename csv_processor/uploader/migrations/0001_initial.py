# Generated by Django 3.2 on 2022-05-08 17:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('bank_account_no', models.CharField(blank=True, max_length=128)),
                ('bank_name', models.CharField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=128)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('street', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='uploader.customer')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
