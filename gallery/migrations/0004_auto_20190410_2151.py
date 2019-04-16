# Generated by Django 2.2 on 2019-04-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20190410_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='dateadded',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='farm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='isfamily',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='isfriend',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='ispublic',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='ownername',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='secret',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='server',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.TextField(null=True),
        ),
    ]