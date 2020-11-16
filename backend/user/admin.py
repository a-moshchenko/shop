from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Customer


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Customer
    list_display = ('id', 'first_name', 'last_name', 'get_image', 'is_staff',
                    'is_active',)
    list_filter = ('first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': (
            'login', 'first_name', 'last_name', 'slug', 'password', 'avatar',
            )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'login', 'first_name', 'last_name', 'slug', 'avatar',
                'password1', 'password2', 'is_staff',
                'is_active',
                )}
         ),
    )
    search_fields = ('first_name', 'last_name',)
    ordering = ('first_name', 'last_name',)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="60" ')

    get_image.short_description = 'аватар'


admin.site.register(Customer, CustomUserAdmin)

