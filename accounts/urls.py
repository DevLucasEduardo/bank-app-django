from django.urls import path
from .views import ClientList, AccountList

urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
    path('accounts/', AccountList.as_view(), name='account-list'),
]