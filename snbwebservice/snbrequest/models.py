from django.db import models
from django.utils.timezone import datetime


# Create your models here.
class ScrapeBuffer(models.Model):
    name = models.CharField(max_length=100, help_text="human readable identifier for scrape run request")
    date_scraped = models.DateField()
    close_spider_page_count = models.IntegerField(null=False)
    css_selector = models.CharField(max_length=255)
    depth_limit = models.IntegerField(null=False)
    json_url_list = models.TextField(null=False)  # Must be JSON list converted from python list


class ScrapeData(models.Model):
    name = models.CharField(max_length=100)

    fk_scrape_buffer = models.ForeignKey(ScrapeBuffer, on_delete=models.SET_NULL, null=True)
    date_scraped = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.name


class BertopicBuffer(models.Model):
    name = models.CharField(max_length=100, help_text="human readable identifier for bertopic run request")
    fk_scrape_data = models.ForeignKey(ScrapeData, on_delete=models.SET_NULL, null=True)
    json_keyword_list = models.TextField(null=True)  # Must be JSON list converted from python list


class BertopicData(models.Model):
    name = models.CharField(max_length=100)
    date_trained = models.DateField(auto_now=True)

    # Must be json data to store as array
    json_topic_data = models.TextField()
    keyword_topic_cluster = models.TextField(null=False)
    fk_scrape_data = models.ForeignKey(ScrapeData, on_delete=models.SET_NULL, null=True)
    fk_bert_buffer = models.ForeignKey(BertopicBuffer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
