from django.urls import path,include
from .views import * #RegisterView,EditView,SettingsView,ProfileView,EditPersonalView
from django.contrib.auth.views import LogoutView
from user.contract_views import *
from user.edit_views import *

app_name = "user"

contract_patterns = [
	path('',ContractsList.as_view(),name="contracts"),
	path('create/',ContractCreate.as_view(),name="contract_create"),
	path('<slug>-<pk>/',ContractView.as_view(),name="contract_detail"),
	path('<pk>/edit/',ContractEdit.as_view(),name="contract_edit"),
	path('<pk>/applications/',ContractApplications.as_view(),name="contract_applications"),
	path('<pk>/applications-<app_pk>/',ContractApplicationAccept,name="application_accept"),
	path('<pk>/applications-<app_pk>/',ContractApplicationDeny,name="application_deny"),
]

edit_patterns = [
	path('personal/',EditPersonalView.as_view(),name="edit_personal"),
	path('contact/',EditContactView.as_view(),name="edit_contact"),
	path('bank-account/',EditBankView.as_view(),name="edit_bank_account"),
	path('occupations/',EditOccupationView.as_view(),name="edit_occupations"),
	path('profile-image/',EditProfileImage.as_view(),name="edit_profile_image"),
]

urlpatterns = [
	path("",ProfileView.as_view(),name="profile"),
	path('logout/',LogoutView.as_view(next_page = "user:login"),name="logout"),
	path('', include("django.contrib.auth.urls")),
	path("register",RegisterView,name="register"),
	path("edit-",include(edit_patterns)),
	path('contracts/',include(contract_patterns)),
]