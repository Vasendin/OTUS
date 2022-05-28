"""cl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Contracts.views as contracts

urlpatterns = [
    # path('', contracts.index),
    # path('organizations/', contracts.index),
    path('', contracts.ContractListView.as_view(), name='main'),
    path('contract/detail/<int:pk>/', contracts.ContractDetailView.as_view(), name='contract_detail'),
    path('contract/create/', contracts.ContractCreateView.as_view(), name='contract_create'),
    path('contract/update/<int:pk>/', contracts.ContractUpdateView.as_view(), name='contract_update'),
    path('organizations/', contracts.OrganizationListView.as_view(), name='organizations'),
    path('organizations/detail/<int:pk>/', contracts.OrganizationDetailView.as_view(), name='organization_detail'),
    path('organizations/create/', contracts.OrganizationCreateView.as_view(), name='organization_create'),
    path('organizations/update/<int:pk>/', contracts.OrganizationUpdateView.as_view(), name='organization_update'),

    path('admin/', admin.site.urls),
]
