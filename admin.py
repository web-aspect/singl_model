from django.contrib import admin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .models import Config


csrf_protect_m = method_decorator(csrf_protect)


class ConfigAdmin(admin.ModelAdmin):
    """
    Настройки сайта.
    
    """

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        model = self.model
        if model.objects.all().count() > 1:
            return super(ConfigAdmin, self).changelist_view(request)
        else:
            obj = model.objects.get_or_create(id=1)[0]
            return redirect(reverse('admin:configuration_%s_change' % \
                    model._meta.module_name, args=(obj.id,)))

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False

admin.site.register(Config, ConfigAdmin)