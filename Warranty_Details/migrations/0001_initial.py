# Generated by Django 3.1.4 on 2020-12-31 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hull_report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warranty_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('1', 'Open'), ('2', 'Item Ready'), ('3', 'Item Shipped'), ('4', 'Compensation'), ('5', 'Close')], default='1', max_length=12)),
                ('section', models.CharField(choices=[('1', 'Hull'), ('2', 'Machinery'), ('3', 'Painting'), ('4', 'Accommodation'), ('5', 'Design'), ('6', 'Management')], max_length=12)),
                ('Importance', models.CharField(choices=[('Critical', 'A'), ('Urgent', 'B'), ('Moderate', 'C'), ('Minor', 'D')], default='Moderate', max_length=12)),
                ('report_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hull_report.hull_report')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
