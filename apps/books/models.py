from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BookPurchase(models.Model):
    title = models.CharField("書籍名", max_length=255)
    isbn = models.CharField("ISBN", max_length=255, null=True, blank=True)
    cover = models.URLField("表紙", null=True, blank=True)
    purchase_at = models.DateField("購入日")
    price = models.DecimalField("価格", max_digits=10, decimal_places=2)
    price_reference_url = models.URLField("価格の参考URL", null=True, blank=True)
    has_apply = models.BooleanField("申請済み", default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "book_purchase"
        verbose_name_plural = "book_purchases"
        db_table = "book_purchases"
