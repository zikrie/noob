from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'HONDA'),
        (PAPERBACK, 'HILUX'),
        (EBOOK, 'TOYOTA'),
    )
    CustomerName = models.CharField(max_length=50)
    PickUpDate = models.DateField(blank=True, null=True)
    IcNum = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    NumOrder = models.IntegerField(blank=True, null=True)
    CarTypes = models.PositiveSmallIntegerField(choices=BOOK_TYPES, blank=True, null=True)
