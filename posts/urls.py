from .api import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('v1/api/testimonials/', views.PostList.as_view(), name='api-list-testimonials'),
]

urlpatterns = format_suffix_patterns(urlpatterns)