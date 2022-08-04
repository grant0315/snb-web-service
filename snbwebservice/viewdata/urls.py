from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index')
]

urlpatterns += [
    path(r'bertopic-results/<int:pk>/', views.bert_result.as_view(), name='bert_result')
]

urlpatterns += [
    path(r'scraped-data-results/<int:pk>/', views.scraped_data_result.as_view(), name='scraped_data_results')
]