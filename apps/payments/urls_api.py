from rest_framework.routers import DefaultRouter
from apps.payments.api.views import PaymentViewSet

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payment")

urlpatterns = router.urls
