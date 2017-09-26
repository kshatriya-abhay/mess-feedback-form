from django.contrib import admin
from hab_app.models import *
from django.apps import apps

app = apps.get_app_config('hab_app')

for model_name, model in app.models.items():
    if model_name!="HostelRoom" and model_name!="HostelRoomOccupantRelation" and model_name!="HostelViewAccess" :
        admin.site.register(model)
