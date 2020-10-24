from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForms

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    form_class = PageForms
    #fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages')

class PageUpdate(UpdateView):
    model = Page
    form_class = PageForms
#fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) + '?ok'

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')

# Create your views here.
#def pages(request):
#pages = get_list_or_404(Page)
#return render(request, 'pages/pages.html', {'pages':pages})
#def page(request, page_id, page_slug):
    #page = get_object_or_404(Page, id=page_id)
    #return render(request, 'pages/page.html', {'page':page})