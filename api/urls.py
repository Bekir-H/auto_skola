from django.urls import re_path as url

#from api.views.auth import AuthenticationView
from api.views.auth import AuthenticationView
from api.views.health import HealthCheckView
from api.views.registration import RegisterView

urlpatterns = [
    # Auth
    url(r"^auth/login/?$", AuthenticationView.as_view(), name="auth"),
    url(r"^registration/?$", RegisterView.as_view(), name="register"),
    url(r"^health/?$", HealthCheckView.as_view(), name='health_check')
]

