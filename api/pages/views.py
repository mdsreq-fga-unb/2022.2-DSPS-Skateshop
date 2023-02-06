from django.views.generic import TemplateView

from company.models import Company
from products.models import Category, Product


MAX_PRODUCTS_PER_CATEGORY = 5


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # get information about the company such as the address, phone number, etc.
        context["company"] = Company.objects.all().first()
        # get the categories that are in the homepage
        context['categories'] = Category.objects.filter(is_in_homepage=True).order_by('-homepage_priority')
        # 5 products of each category
        product_list = []
        missing_product_quantity_per_category = []
        for category in context['categories']:
            category_products = Product.objects.filter(category=category)[:MAX_PRODUCTS_PER_CATEGORY]
            product_list.extend(category_products)
            missing_product_quantity_per_category.append(MAX_PRODUCTS_PER_CATEGORY - len(category_products))
        context['product_list'] = product_list
        # zip the categories with the quantity of products that are missing to complete the 5 products
        context['categories'] = zip(context['categories'], missing_product_quantity_per_category)
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["company"] = Company.objects.all().first()
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context["company"] = Company.objects.all().first()
        return context
