from django.views.generic import TemplateView

from company.models import Company
from products.models import Category, Product
from faq.models import FAQ


MAX_PRODUCTS_PER_CATEGORY = 5


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # get information about the company such as the address, phone number, etc.
        context["company"] = Company.objects.all().first()
        # get the categories that are in the homepage
        context['categories'] = []
        categories = Category.objects.filter(is_in_homepage=True).order_by('-homepage_priority')
        # TODO: do the following queries with SQL instead of the Django imcomplete ORM. F
        # 5 products of each category
        product_list = Product.objects.all()
        product_list_per_category = []
        for category in categories:
            tmp_list = product_list.filter(
                may_be_in_homepage=True, category=category
            )
            product_without_discount = [p for p in tmp_list if not p.has_discount]
            product_list_per_category.extend(
                product_without_discount[:MAX_PRODUCTS_PER_CATEGORY]
            )
            if len(product_without_discount) > 0:
                context['categories'].append(category)
        context['product_list'] = product_list_per_category
        # products with offers
        product_with_offer_list = []
        for product in product_list.filter(limited_time_offer__isnull=False):
            if product.has_discount:
                product_with_offer_list.append(product)
        context['product_with_offer_list'] = product_with_offer_list
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
    
class FaqPageView(TemplateView):
    template_name = 'faq.html'

    def get_context_data(self, **kwargs):
        context = super(FaqPageView, self).get_context_data(**kwargs)
        context["faqs"] = FAQ.objects.all()
        return context
