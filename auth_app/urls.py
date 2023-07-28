from django.urls import path
from .views import addData, listData, listDataDetail, updateData, deleteData, overViews

urlpatterns = [
    path('', overViews, name='overViews'),
    path('listData', listData, name='listData'),
    path('addData', addData, name='addData'),
    path('listDataDetail/<str:id>/', listDataDetail, name='listDataDetail'),
    path('updateData/<str:id>/', updateData, name='updateData'),
    path('deleteData/<str:id>/', deleteData, name='deleteData')
]   