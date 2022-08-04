from django.contrib import admin

from .forms import SubRubricForm
from .models import SuperRubric, SubRubric, AdvUser, AdditionalImage, Bb


class SubRubricInline(admin.TabularInline):
    model = SubRubric

class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)

class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm



class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric','title','content','author','create_at')
    fields = (('rubric','author'), 'title' , 'content','price',
              'contacts','image','is_active')
    inlines = (AdditionalImageInline,)




admin.site.register(Bb,BbAdmin)
admin.site.register(AdvUser)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric,SubRubricAdmin)

