from django.urls import path, include
from rest_framework.routers import SimpleRouter

from API.resources import UserViewSet, TransactionViewSet, SeriviceViewSet, PointZeroView, PointNonZeroView

router = SimpleRouter()
router.register('user', UserViewSet)
router.register('transaction', TransactionViewSet)
router.register('type_of_service', SeriviceViewSet)
router.register('get_zero_point', PointZeroView)
router.register('get_non_zero_point', PointNonZeroView)

urlpatterns = [

    path('api/', include(router.urls)),
]