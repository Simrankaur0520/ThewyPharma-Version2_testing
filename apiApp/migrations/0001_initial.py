# Generated by Django 4.0.3 on 2023-12-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('Points', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='cart_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='categoryy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('category_colour', models.TextField()),
                ('category_image', models.TextField()),
                ('category_banner', models.TextField()),
                ('category_banner_mobile', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('deactivated_products', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.TextField()),
                ('customer_name', models.TextField()),
                ('email', models.TextField()),
                ('contact', models.TextField()),
                ('Address_line1', models.TextField()),
                ('Address_line2', models.TextField()),
                ('city', models.TextField()),
                ('pincode', models.TextField()),
                ('state', models.TextField()),
                ('Country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True)),
                ('speciality', models.TextField(blank=True)),
                ('available', models.TextField(blank=True)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='images_and_banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.TextField()),
                ('mobile_image', models.TextField(blank=True)),
                ('product_id', models.TextField(blank=True)),
                ('discount', models.TextField(blank=True)),
                ('type', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='noLoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField()),
                ('user_id', models.TextField(blank=True, null=True)),
                ('placed_at', models.DateField(auto_now_add=True, null=True)),
                ('product_details', models.TextField(blank=True, null=True)),
                ('Total_amount', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('placed', 'PLACED'), ('Processed', 'processed'), ('dispatched', 'DISPATCHED'), ('on the way', 'On the way'), ('delivered', 'DELIVERED'), ('CANCELLED', 'cancelled'), ('RETURNED', 'returned')], default='Placed', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_product', models.TextField()),
                ('order_amount', models.TextField()),
                ('order_payment_id', models.TextField()),
                ('isPaid', models.BooleanField(default=False)),
                ('order_date', models.TextField(default='2023-12-14 22:54:11.907337+05:30')),
                ('user_id', models.TextField(null=True)),
                ('order_status', models.TextField(blank=True)),
                ('admin_placed_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('price', models.TextField(blank=True)),
                ('discount', models.TextField(blank=True)),
                ('size', models.TextField(blank=True)),
                ('benefits', models.TextField(blank=True)),
                ('ingredients', models.TextField(blank=True)),
                ('how_to_use', models.TextField(blank=True)),
                ('how_we_make_it', models.TextField(blank=True)),
                ('nutrition', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('sibling_product', models.TextField(blank=True)),
                ('HSN', models.TextField(blank=True)),
                ('SKU', models.TextField(blank=True)),
                ('tax', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('add_line_1', models.TextField(blank=True)),
                ('add_line_2', models.TextField(blank=True, null=True)),
                ('landmark', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True)),
                ('state', models.TextField(blank=True)),
                ('country', models.TextField(blank=True)),
                ('pincode', models.TextField(blank=True)),
                ('phone_no', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(blank=True)),
                ('product_id', models.TextField()),
                ('size', models.TextField()),
                ('price_per_unit', models.TextField(blank=True)),
                ('quantity', models.TextField(default=0)),
                ('image', models.TextField(blank=True, null=True)),
                ('no_login_id', models.TextField(blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField(blank=True)),
                ('email', models.TextField()),
                ('gender', models.TextField()),
                ('dob', models.TextField(blank=True)),
                ('phone_code', models.TextField()),
                ('phone_no', models.TextField()),
                ('password', models.TextField(blank=True)),
                ('token', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('admin_create_status', models.BooleanField(default=False)),
            ],
        ),
    ]