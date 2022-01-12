from django.contrib import admin

import app1.models
# Register your models here.
admin.site.register(app1.models.Board)
admin.site.register(app1.models.Reply)