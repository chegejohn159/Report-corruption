from django.contrib import admin
from .models import *
# Register your models here.

class corruptionAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(corruptionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['police'].queryset = user.objects.filter(is_police=True)
        return form

class userAdmin(admin.ModelAdmin):
    def count(self, obj):
        return user.corruption_set.count()

admin.site.register(complain)
admin.site.register(entity)
admin.site.register(county)
admin.site.register(corruptiontype)
admin.site.register(corruption,corruptionAdmin)
admin.site.register(user,userAdmin)
admin.site.register(reportchallenges)

