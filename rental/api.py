from rest_framework import routers
# from core import views as myapp_views


# router = routers.DefaultRouter()
# router.register(r'friends', myapp_views.FriendViewset)
# router.register(r'belongings', myapp_views.BelongingViewset)
# router.register(r'borrowings', myapp_views.BorrowedViewset)

from .api_views import FriendViewset
from .api_views import BelongingViewset
from .api_views import BorrowedViewset

router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'belongings', BelongingViewset)
router.register(r'borrowings', BorrowedViewset)
