from django.urls import path
from . import viewset

urlpatterns = [
    path('recycling_company/', viewset.RecyclingCompanyListView.as_view()),
    path('collection_points/', viewset.CollectionPointsListView.as_view()),
    path('collection_neighbordhoods/', viewset.CollectsNeighborhoodsListView.as_view()),
]