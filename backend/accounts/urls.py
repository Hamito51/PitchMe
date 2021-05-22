from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import UserViewSet

router = DefaultRouter()
router.register('sign-up', UserViewSet, basename='sign-up')

urlpatterns = [
                path('auth/', include('djoser.urls')),
                path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
