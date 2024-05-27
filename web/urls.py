from django.urls import path
from web.views import main_view, obj_list, obj_single, obj_create, obj_delete, obj_modify, obj_statistic

urlpatterns = [
    path('', main_view),
    path('object', obj_list),
    path('object/<int:id>/', obj_single),
    path('object/<int:id>/statistic/', obj_statistic),
    path('object/create', obj_create),
    path('object/delete/<int:id>', obj_delete),
    path('object/modify/<int:id>', obj_modify),
]