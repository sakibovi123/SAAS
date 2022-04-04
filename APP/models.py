from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from djrichtextfield.models import RichTextField



class Package(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    package_title = models.CharField(max_length=255, null=True, blank=True)
    package_description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.FloatField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Package Name: {self.package_title}"

    def get_absolute_url(self):
        return f"/package/{self.package_title}/"

    def save(self, *args, **kwargs):
        if self.discount:
            self.price = self.price * self.discount / 100
        super(Order, self).save(*args, **kwargs)


class Cart(models.Model):
    created_at = models.DateField(
        default=date.today
    )
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    created_at = models.DateField(default=date.today)
    invoice_no = models.CharField(
        max_length=255, null=True, blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    first_name = models.CharField(
        max_length=255,
        null=True, blank=True
    )
    last_name = models.CharField(
        max_length=255,
        null=True, blank=True
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.invoice_no

    def get_absolute_url(self):
        return f"/order/{self.invoice_no}/"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)




    

    

