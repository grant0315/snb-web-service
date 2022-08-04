from django.contrib import admin

# Register your models here.
from snbrequest.models import BertopicData, ScrapeData, BertopicBuffer, ScrapeBuffer


@admin.register(BertopicData)
class BertopicDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'json_topic_data', 'keyword_topic_cluster',
                    'fk_scrape_data', 'fk_bert_buffer')


@admin.register(ScrapeData)
class ScrapeDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'fk_scrape_buffer', 'content')


@admin.register(BertopicBuffer)
class BertopicBufferAdmin(admin.ModelAdmin):
    list_display = ('name', 'fk_scrape_data', 'json_keyword_list')


@admin.register(ScrapeBuffer)
class ScrapeBufferAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_scraped', 'close_spider_page_count',
                    'css_selector', 'depth_limit', 'json_url_list')
