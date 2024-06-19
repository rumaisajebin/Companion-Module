from django.urls import path
from .views import *

urlpatterns = [
    path('Profile_list', CompanionProfileListView.as_view(), name='Profile_list'),
    path('Profile_create', CompanionProfileCreateView.as_view(), name='Profile_create'),
    path('Profile_update/<int:pk>/', CompanionProfileUpdateView.as_view(), name='Profile_update'),
    path('Profile_delete/<int:id>/', CompanionProfileDeleteView.as_view(), name='Profile_delete'),
    path('Profile_detailview/<int:id>/', CompanionProfileDetailListView.as_view(), name='Profile_detailview'),
]