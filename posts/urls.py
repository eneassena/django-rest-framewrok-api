from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

# urlpatterns v1.2
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls


# urlpatterns v1.1
# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users-viewset/', UserViewSet.as_view({'get': 'list'})),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('posts/', PostList.as_view()),
#     path('posts-viewset/', PostViewSet.as_view({'get': 'list'})),
#     path('posts/<int:pk>/', PostDetail.as_view()),

# ]
