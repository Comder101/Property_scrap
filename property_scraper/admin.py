from django.contrib import admin
from .models import ScrapingLog, CronJobSettings

admin.site.register(ScrapingLog)
admin.site.register(CronJobSettings)