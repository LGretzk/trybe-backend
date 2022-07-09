from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'goals', views.GoalViewSet,basename="goals")
# router.register(r'users', views.UserViewSet,basename="user")

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]