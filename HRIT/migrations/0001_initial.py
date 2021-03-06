from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=120)),
                ('make', models.CharField(max_length=120)),
                ('purchase_date', models.DateField()),
            ],
            options={
                'db_table': 'computers',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('computers', models.ManyToManyField(blank=True, null=True, to='HRIT.Computer')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRIT.Department')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Training_Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('maxAttendees', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'training_programs',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='training_programs',
            field=models.ManyToManyField(blank=True, null=True, to='HRIT.Training_Program'),
        ),
    ]
