from django.urls import re_path as url

from api.admin.views.registration import CreateUserView
from api.admin.views.user import UpdateUserView

admin_urlpatterns = [
    # Admin Endpoints
    url(r"^admin/registration/?$", CreateUserView.as_view(), name="admin_account_create"),
    url(r"^admin/user/(?P<pk>[0-9]+)/?$", UpdateUserView.as_view(), name="admin_update_user"),
]
