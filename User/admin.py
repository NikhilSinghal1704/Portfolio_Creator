from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # List display options (list view in admin)
    list_display = ('user', 'image_tag', 'info_preview', 'has_image')
    list_filter = ('user',)
    search_fields = ('user__username', 'user__email', 'info')

    # Fields to show in the profile creation/edit form
    fields = ('user', 'image', 'image_preview')

    # Make some fields read-only
    readonly_fields = ('image_preview',)

    # Custom display of image in the list view
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />', obj.image.url)
        return '-'
    image_tag.short_description = 'Profile Picture'

    # Show preview of profile picture in the form view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height: 150px; border-radius: 50%;" />', obj.image.url)
        return 'No Image Uploaded'
    image_preview.short_description = 'Profile Picture Preview'

    # Preview of profile info (truncate long text)
    def info_preview(self, obj):
        return (obj.info[:75] + '...') if obj.info and len(obj.info) > 75 else obj.info
    info_preview.short_description = 'Info Preview'

    # Check if a profile has a custom image or is using the default
    def has_image(self, obj):
        return obj.image and obj.image.name != 'default.jpg'
    has_image.boolean = True  # Displays as a boolean icon
    has_image.short_description = 'Custom Image'
