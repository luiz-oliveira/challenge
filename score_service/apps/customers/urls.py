from rest_framework_mongoengine import routers
from .views import Customer

# Mongo routers
router = routers.DefaultRouter()
router.register(r'mongo', Customer)

urlpatterns = [] + router.urls