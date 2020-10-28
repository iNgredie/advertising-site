from rest_framework import routers

from .views import AdViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'ad', AdViewSet)

urlpatterns += router.urls