from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from snbrequest.models import BertopicData, ScrapeData, BertopicBuffer, ScrapeBuffer


# Create your views here.
def index(request):
    """View function for home page of website"""

    bertopic_results_list = BertopicData.objects.order_by('-date_trained')
    scraped_data_results_list = ScrapeData.objects.order_by('-date_scraped')

    context = {
        'bertopic_results': bertopic_results_list,
        'scraped_data_results': scraped_data_results_list,
    }

    return render(request, 'snb_results.html', context=context)


class bert_result(DetailView):
    model = BertopicData
    template_name = 'bert_results.html'
    context_object_name = 'bert_result'


class scraped_data_result(DetailView):
    model = ScrapeData
    template_name = 'scrape_data_results.html'
    context_object_name = 'scraped_data_result'
