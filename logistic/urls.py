from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, test_view

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("stocks", StockViewSet)
router.register("test", test_view)

urlpatterns = router.urls
