from django.urls import re_path as url

from api.admin.urls import admin_urlpatterns
from api.views.registration import ActivateAccountView
from api.views.health import HealthCheckView
from api.views.auth import AuthenticationView
from api.views.user import UserView

urlpatterns = [
    # Auth
    url(r"^auth/login/?$", AuthenticationView.as_view(), name="auth"),
    url(r"^auth/activate/(?P<token>\w{0,32})/?$", ActivateAccountView.as_view(), name="activate_account"),

    url(r"^health/?$", HealthCheckView.as_view(), name='health_check'),

    # User
    url(r"^current/?$", UserView.as_view(), name="current_user")
] + admin_urlpatterns
