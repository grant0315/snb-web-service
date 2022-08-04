from django.shortcuts import render
from django.views.generic.detail import DetailView
from snbrequest.models import BertopicData, ScrapeData, BertopicBuffer, ScrapeBuffer


# Create your views here.
def index(request):
    """View function for home page of website"""

    context = {}

    return render(request, 'index.html', context=context)


class bert_results(DetailView):
    model = BertopicData
    template_name = 'viewdata/bert_results.html'