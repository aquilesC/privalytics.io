from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from accounts.views import SignUpView, ActivateView, DashboardView, CreateWebsite, AccountView, SubscriptionView


waiting_list_view = TemplateView.as_view(template_name='accounts/waiting_list.html')

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('waiting-list', waiting_list_view, name='waiting-list'),
    path('signup/<str:account_type>', SignUpView.as_view(), name='signup-account-type'),
    path('activate/<str:uidb64>/<str:token>', ActivateView.as_view(), name='activate'),
    path('login', LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('account', AccountView.as_view(), name='account'),
    path('subscriptions', SubscriptionView.as_view(), name='subscription'),
    path('account/new-website', CreateWebsite.as_view(), name='create-website'),
    path('logout', LogoutView.as_view(), name='logout'),
]
