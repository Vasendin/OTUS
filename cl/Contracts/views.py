from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Contract, Organization
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .forms import ContractCreateForm, OrganizationCreateForm


# def index(request):
#     all_contracts = Contract.objects.all()
#     # print(all_contracts)
#     context = {
#         'all_contracts': all_contracts
#     }
#     return render(request, 'index.html', context=context)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class ContractListView(ListView):
    model = Contract


class ContractDetailView(PageTitleMixin, DetailView):
    model = Contract
    page_title = 'Contract detail'


class ContractCreateView(CreateView):
    model = Contract
    success_url = reverse_lazy('main')
    form_class = ContractCreateForm
    # fields = '__all__'


class ContractUpdateView(UpdateView):
    model = Contract
    success_url = reverse_lazy('main')
    fields = '__all__'


class OrganizationListView(ListView):
    model = Organization


class OrganizationDetailView(PageTitleMixin, DetailView):
    model = Organization
    page_title = 'Organization detail'


class OrganizationCreateView(CreateView):
    model = Organization
    success_url = reverse_lazy('main')
    form_class = OrganizationCreateForm
    # fields = '__all__'


class OrganizationUpdateView(UpdateView):
    model = Organization
    success_url = reverse_lazy('main')
    fields = '__all__'
