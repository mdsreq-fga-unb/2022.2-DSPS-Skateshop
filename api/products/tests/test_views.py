import pytest
from django.urls import resolve, reverse

from .factories import ProductFactory

pytestmark = pytest.mark.django_db


class TestProductListView:
    def test_reverse_resolve(self):
        assert reverse("products:list") == "/products/"
        assert resolve("/products/").view_name == "products:list"

        url = reverse("products:list_by_category", kwargs={"slug": "test-slug"})
        assert url == "/products/category/test-slug/"

        view_name = resolve("/products/category/test-slug/").view_name
        assert view_name == "products:list_by_category"

    def test_status_code(self, client, category):
        response = client.get(reverse("products:list"))
        assert response.status_code == 200

        response = client.get(
            reverse("products:list_by_category", kwargs={"slug": category.slug})
        )
        assert response.status_code == 200


class TestProductDetailView:
    def test_reverse_resolve(self, product):
        url = reverse("products:detail", kwargs={"slug": product.slug})
        assert url == f"/products/{product.slug}/"

        view_name = resolve(f"/products/{product.slug}/").view_name
        assert view_name == "products:detail"

    def test_status_code(self, client):
        product = ProductFactory(is_available=True)
        url = reverse("products:detail", kwargs={"slug": product.slug})
        response = client.get(url)
        assert response.status_code == 200
