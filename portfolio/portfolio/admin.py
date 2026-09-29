from django.contrib import admin

from .models import (
    AboutCard,
    ContactMessage,
    Experience,
    Project,
    SiteProfile,
    Skill,
    SocialLink,
)


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "email",
        "available",
        "resume",
        "updated_at",
    )


@admin.register(AboutCard)
class AboutCardAdmin(admin.ModelAdmin):
    list_display = (
        "icon",
        "title",
        "sort_order",
    )
    ordering = ("sort_order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "featured",
        "sort_order",
        "created_at",
    )
    list_filter = ("featured",)
    search_fields = (
        "title",
        "short_description",
        "technologies",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "period",
        "sort_order",
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "url",
        "sort_order",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "is_read",
        "created_at",
    )
    list_filter = ("is_read",)
    readonly_fields = ("created_at",)