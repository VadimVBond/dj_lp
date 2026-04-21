from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    context = {
        'page_title': _('Welcome to Our Platform'),
        'hero_title': _('Build Something Amazing'),
        'hero_subtitle': _('The fastest way to create powerful digital solutions for your business.'),
        'start_now': _('Start Now'),
        'features_title': _('Why Choose Us'),
        'features_subtitle': _('Discover the features that make our platform stand out.'),
        'feature_1_title': _('Lightning Fast'),
        'feature_1_desc': _('Optimized performance for the best user experience.'),
        'feature_2_title': _('Secure by Default'),
        'feature_2_desc': _('Enterprise-grade security to protect your data.'),
        'feature_3_title': _('Flexible Layout'),
        'feature_3_desc': _('Customize everything to match your brand.'),
        'cta_title': _('Ready to Get Started?'),
        'cta_subtitle': _('Join thousands of satisfied customers today.'),
        'email_placeholder': _('Enter your email'),
        'subscribe': _('Subscribe'),
    }
    return render(request, 'index.html', context)
