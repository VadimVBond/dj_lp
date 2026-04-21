from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    context = {
        "page_title": _("Landing Page"),
        "hero_title": _("Modern Solutions for Your Business"),
        "hero_subtitle": _(
            "We help you build better products with our advanced framework and expert consulting."
        ),
        "start_now": _("Start Now"),
        "features_title": _("Our Features"),
        "features_subtitle": _(
            "Discover why thousands of companies choose our platform for their digital needs."
        ),
        "feature_1_title": _("High Performance"),
        "feature_1_desc": _(
            "Lightning fast response times and optimized resource usage."
        ),
        "feature_2_title": _("Secure by Design"),
        "feature_2_desc": _(
            "Enterprise-grade security features built into every layer."
        ),
        "feature_3_title": _("Easy Integration"),
        "feature_3_desc": _("Connect with your favorite tools in minutes, not days."),
        "cta_title": _("Ready to get started?"),
        "cta_subtitle": _(
            "Join our newsletter to stay updated with the latest news and offers."
        ),
        "email_placeholder": _("Enter your email"),
        "subscribe": _("Subscribe"),
        "copyright": _("All rights reserved."),
    }
    return render(request, "index.html", context)
