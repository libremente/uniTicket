from django.contrib import admin

from .models import *
from .admin_inlines import *

class AbstractAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    class Media:
        js = ('js/textarea-autosize.js',)
        css = {'all': ('css/textarea-small.css',),}


@admin.register(OrganizationalStructureFunction)
class OrganizationalStructureFunctionAdmin(AbstractAdmin):
    pass


@admin.register(OrganizationalStructureType)
class OrganizationalStructureTypeAdmin(AbstractAdmin):
    pass


@admin.register(OrganizationalStructure)
class OrganizationalStructureAdmin(AbstractAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'structure_type',
                    'description', 'is_active')
    list_filter = ('structure_type', 'is_active')
    list_editable = ('is_active',)
    inlines = [OrganizationalStructureLocationInline,
               OrganizationalStructureOfficeInline,]


@admin.register(OrganizationalStructureOffice)
class OrganizationalStructureOfficeAdmin(AbstractAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'organizational_structure', 'is_active')

    list_filter = ('organizational_structure',
                   'is_active')

    list_editable = ('is_active',)

    inlines = [OrganizationalStructureOfficeEmployeeInline,
               OrganizationalStructureOfficeLocationInline,]


#@admin.register(TipoDotazione)
#class TipoDotazioneAdmin(admin.ModelAdmin):
    #list_display = ('nome', 'descrizione')

    #class Media:
        #js = ('js/textarea-autosize.js',)
        #css = {'all': ('css/textarea-small.css',),}

#@admin.register(Locazione)
#class LocazioneAdmin(admin.ModelAdmin):
    #list_display = ('nome', 'indirizzo', 'descrizione_breve',)

    #class Media:
        #js = ('js/textarea-autosize.js',)
        #css = {'all': ('css/textarea-small.css',),}


# @admin.register(OrganizationalStructureFunction)
# class OrganizationalStructureFunction(AbstractAdmin):
    # pass
