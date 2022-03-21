# Generated by Django 3.0.7 on 2021-04-04 20:16

import InvenTree.fields
import InvenTree.models
import InvenTree.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_owner_model'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0058_stockitem_packaging'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='delete_on_deplete',
            field=models.BooleanField(default=False, help_text='Delete this Stock Item when stock is depleted', verbose_name='Delete on deplete'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Select Owner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_items', to='users.Owner', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='stockitemattachment',
            name='attachment',
            field=models.FileField(help_text='Select file to attach', upload_to=InvenTree.models.rename_attachment, verbose_name='Attachment'),
        ),
        migrations.AlterField(
            model_name='stockitemattachment',
            name='comment',
            field=models.CharField(blank=True, help_text='File comment', max_length=100, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='stockitemattachment',
            name='upload_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='upload date'),
        ),
        migrations.AlterField(
            model_name='stockitemattachment',
            name='user',
            field=models.ForeignKey(blank=True, help_text='User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='stockitemtracking',
            name='link',
            field=InvenTree.fields.InvenTreeURLField(blank=True, help_text='Link to external page for further information', verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='stockitemtracking',
            name='notes',
            field=models.CharField(blank=True, help_text='Entry notes', max_length=512, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='stockitemtracking',
            name='quantity',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='stockitemtracking',
            name='title',
            field=models.CharField(help_text='Tracking entry title', max_length=250, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='stocklocation',
            name='description',
            field=models.CharField(blank=True, help_text='Description (optional)', max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='stocklocation',
            name='name',
            field=models.CharField(help_text='Name', max_length=100, validators=[InvenTree.validators.validate_tree_name], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='stocklocation',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Select Owner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_locations', to='users.Owner', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='stocklocation',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='stock.StockLocation', verbose_name='parent'),
        ),
    ]
