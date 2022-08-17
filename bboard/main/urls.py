from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.static import serve
from .views import index, other_page, BBLoginView, profile, BBLogoutView, ChangeUserInfoView, BBPasswordChangeView, \
    RegisterDoneView, RegisterUserView, DeleteUserView, by_rubric, detail, profile_bb_add, profile_bb_detail, \
    profile_bb_change, profile_bb_delete, BbListView, BbDetailView

urlpatterns = [
    path('Bb/', BbListView.as_view()),
    path('Bb/<int:pk>/', BbDetailView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register_user'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/change/<int:pk>', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>', profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add')
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve))),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
