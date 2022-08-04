from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('bertopicresult/<int:pk>', views.bert_results.as_view(), name='bert_result')
]