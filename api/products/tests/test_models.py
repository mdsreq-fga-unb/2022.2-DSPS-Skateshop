import pytest

from ..models import Product
from .factories import ProductFactory

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test___str__(self, category):
        assert category.__str__() == category.name
        assert str(category) == category.name

    def test_get_absolute_url(self, category):
        url = category.get_absolute_url()
        assert url == f"/products/category/{category.slug}/"


class TestProductModel:
    def test___str__(self, product):
        assert product.__str__() == product.name
        assert str(product) == product.name

    def test_get_absolute_url(self, product):
        url = product.get_absolute_url()
        assert url == f"/products/{product.slug}/"

    def test_available_manager(self):
        ProductFactory(is_available=True)
        ProductFactory(is_available=False)

        assert Product.objects.all().count() == 2
        assert Product.available.all().count() == 1
