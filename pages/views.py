from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class PricingPageView(TemplateView):
    template_name = "pricing.html"

class TermsPageView(TemplateView):
    template_name = "terms.html"

class PrivacyPageView(TemplateView):
    template_name = "privacypolicy.html"

# Create your views here.
