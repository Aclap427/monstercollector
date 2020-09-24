from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('monsters/', views.monsters_index, name='index'),
  path('monsters/<int:monster_id>/', views.monsters_detail, name='detail'),
  path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
  path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
  path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),
  path('monsters/<int:monster_id>/add_rental/', views.add_rental, name='add_rental'),
  path('monsters/<int:monster_id>/assoc_extra/<int:extra_id>/', views.assoc_extra, name='assoc_extra'),
  path('monsters/<int:monster_id>/unassoc_extra/<int:extra_id>/', views.unassoc_extra, name='unassoc_extra'),
  path('extras/', views.ExtraList.as_view(), name='extras_index'),
  path('extras/<int:pk>/', views.ExtraDetail.as_view(), name='extras_detail'),
  path('extras/create/', views.ExtraCreate.as_view(), name='extras_create'),
  path('extras/<int:pk>/update/', views.ExtraUpdate.as_view(), name='extras_update'),
  path('extras/<int:pk>/delete/', views.ExtraDelete.as_view(), name='extras_delete'),
]