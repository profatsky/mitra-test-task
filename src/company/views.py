from django.views.generic import TemplateView, ListView

from .models import Bargain, Document


class IndexView(TemplateView):
    template_name = 'company/index.html'


class BargainsListView(ListView):
    template_name = 'company/bargains_list.html'
    queryset = Bargain.objects.all()
    context_object_name = 'bargains_list'
    paginate_by = 3


class DocumentsListView(ListView):
    template_name = 'company/documents_list.html'
    queryset = Document.objects.all()
    context_object_name = 'documents_list'
    paginate_by = 3


class AboutUsView(TemplateView):
    template_name = 'company/about_us.html'


class ContactsView(TemplateView):
    template_name = 'company/contacts.html'
