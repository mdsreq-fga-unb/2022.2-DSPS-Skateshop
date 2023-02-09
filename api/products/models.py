import decimal
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel  # Model with created and modified columns
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.functional import cached_property


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')
    is_in_homepage = models.BooleanField(default=False)
    homepage_priority = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:list_by_category', kwargs={'slug': self.slug})


class LimitedTimeOffer(TimeStampedModel):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    # somente pode ser usado um dos seguintes dois campos por vez
    relative_discount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(95)],
        blank=True, null=True,
    )
    absolute_discount = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, null=True,
    )

    class Meta:
        verbose_name = 'limited_time_offer'
        verbose_name_plural = 'limited_time_offers'

    def __str__(self):
        s = "{:03d}".format(self.id)
        s += ', ' + self.start_datetime.strftime('%d/%m %H:%M')
        s += ' até ' + self.end_datetime.strftime('%d/%m %H:%M')
        if self.relative_discount is not None:
            s += ', -' + str(self.relative_discount) + '%'
        else:
            s += ', -' + 'R$' + str(self.absolute_discount)
        return s

    def get_absolute_url(self):
        return reverse('products:list_by_offer', kwargs={'id': self.id})

    def clean(self):
        if self.relative_discount is not None and self.absolute_discount is not None:
            raise ValidationError("Somente um dos campos pode ser preenchido. Escolha o desconto percentual ou o desconto absoluto.")
        if self.relative_discount is None and self.absolute_discount is None:
            raise ValidationError("Preencha somente um dos campos. Escolha o desconto percentual ou o desconto absoluto.")

    def get_hours_until_end(self):
        return (self.end_datetime - timezone.now()).total_seconds() // 3600

    def get_discounted_price(self, base_price):
        # conferir se a promocao ainda esta em dia
        if self.start_datetime > timezone.now() or self.end_datetime < timezone.now():
            return base_price

        if self.relative_discount is not None:
            return base_price * (100 - self.relative_discount) / 100

        # TODO: refatorar validacao do desconto absoluto em relacao ao preco base
        # se o desconto absoluto for maior que 95% do preco base,
        if self.absolute_discount > (base_price * decimal.Decimal(0.95)):
            # nao aplica desconto na pratica
            return base_price

        return base_price - self.absolute_discount

    def is_discount_absolute(self):
        return self.absolute_discount is not None


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')
    image = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    # este eh o preco base do produto, que eh usado para calcular o preco com desconto
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    limited_time_offer = models.ForeignKey(
        LimitedTimeOffer, related_name='products',
        on_delete=models.SET_NULL, null=True, blank=True
    )
    may_be_in_homepage = models.BooleanField(default=True)


    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    @property
    def price(self):
        if self.limited_time_offer is not None:
            return self.limited_time_offer.get_discounted_price(self.base_price)
        return self.base_price

    # TODO: refatorar forma de ver se o produto esta em promocao
    @property
    def has_discount(self):
        return self.price < self.base_price

    @property
    def display_hours_until_discount_end(self):
        return self.limited_time_offer.get_hours_until_end()
    
    @cached_property
    def is_discount_absolute(self):
        # true eh absoluto, false eh percentual
        return self.limited_time_offer.is_discount_absolute()

    @cached_property
    def absolute_discount(self):
        # true eh absoluto, false eh percentual
        return self.limited_time_offer.absolute_discount

    @cached_property
    def relative_discount(self):
        # true eh absoluto, false eh percentual
        return self.limited_time_offer.relative_discount
