from django.urls import path
from. views import HomePageView, PrivacyPageView, PricingPageView, TermsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("pricing/", PricingPageView.as_view(), name="pricing"),
    path("privacy-policy/", PrivacyPageView.as_view(), name="privacypolicy"),
    path("terms-and-conditions/", TermsPageView.as_view(), name="terms"),

]