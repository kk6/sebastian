# Generated by Django 2.2.6 on 2019-11-02 19:23
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="BookPurchase",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="書籍名")),
                (
                    "isbn",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="ISBN"
                    ),
                ),
                ("cover", models.URLField(blank=True, null=True, verbose_name="表紙")),
                ("purchase_at", models.DateField(verbose_name="購入日")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="価格"
                    ),
                ),
                (
                    "price_reference_url",
                    models.URLField(blank=True, null=True, verbose_name="価格の参考URL"),
                ),
                ("has_apply", models.BooleanField(default=False, verbose_name="申請済み")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "book_purchase",
                "verbose_name_plural": "book_purchases",
                "db_table": "book_purchases",
            },
        )
    ]