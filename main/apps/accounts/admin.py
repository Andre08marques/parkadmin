from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Permissions", {"fields": ("first_name", "last_name", "is_staff", "unidade", "is_superuser", "is_active", "groups", "user_permissions")}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": (
#                 "username", "password1", "password2", "unidade", "email", "is_superuser", "is_staff",
#                 "is_active"
#             )}
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)
# admin.site.register(CustomUser, CustomUserAdmin)