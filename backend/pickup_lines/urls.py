# from rest_framework import routers
from django.urls import path
from .views import PickupLineCreateView, PickupLinesView


urlpatterns = [
    path('pickup-lines', PickupLinesView.as_view()),
    path('create-new', PickupLineCreateView.as_view()),
]


# router = routers.DefaultRouter()
# router.register(r'create-new', PickupLineCreateView)
# router.register(r'pickup-lines', PickupLinesView)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

