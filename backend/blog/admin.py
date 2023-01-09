''' imports '''
from django.contrib import admin
from .models import Profile, Post, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ''' register profile model '''
    model = Profile


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ''' register tag model '''
    model = Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ''' register post model '''
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True
