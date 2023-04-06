from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'company/index.html'


class AboutUsView(TemplateView):
    template_name = 'company/about_us.html'


class ContactsView(TemplateView):
    template_name = 'company/contacts.html'
