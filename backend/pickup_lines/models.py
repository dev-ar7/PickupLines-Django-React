from django.db import models


class PickupLines(models.Model):

    CATEGORY = [
        ('BEST', 'Best'),
        ('CUTE', 'Cute'),
        ('FUNNY', 'Funny'),
        ('ROMANTIC', 'Romantic')
    ]

    line = models.CharField(max_length=500, blank=False, null=False)
    cat = models.CharField(max_length=8, choices=CATEGORY, blank=False, null=False)
    tag = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.line