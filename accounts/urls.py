from django.urls import path
from .views import ClientList, AccountList, ClientDetail, AccountDetail

urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>', ClientDetail.as_view(), name='client-detail'),
    path('accounts/', AccountList.as_view(), name='account-list'),
    path('accounts/<int:pk>', AccountDetail.as_view(), name='account-detail'),
]