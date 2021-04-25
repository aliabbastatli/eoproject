from django.urls import path, include
from .views import (ExampleListAPIView,
                    ExampleUpdateAPIView,
                    DestroyAPIView,
                    )

app_name = "esp"
urlpatterns = [
    path('list', ExampleListAPIView.as_view(), name='list'),
    path('update/<slug>', ExampleUpdateAPIView.as_view(), name='update'), 
]