from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from models import *


admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(Task)