from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('feature/<int:feature_id>', views.feature, name='feature'),
    path('trailers/', views.TrailerListView.as_view(), name='trailers'),
    path('trailers/<int:pk>', views.TrailerDetailView.as_view(), name='trailer-detail'),
    path('search/', views.search, name='search'),
    path('mytrailers/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed')

]