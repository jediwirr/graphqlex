''' imports '''
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from blog import models

class UserType(DjangoObjectType):
    ''' register user model '''
    class Meta:
        ''' register user model '''
        model = get_user_model()


class AuthorType(DjangoObjectType):
    ''' register profile model '''
    class Meta:
        ''' register profile model '''
        model = models.Profile


class PostType(DjangoObjectType):
    ''' register post model '''
    class Meta:
        ''' register post model '''
        model = models.Post


class TagType(DjangoObjectType):
    ''' register tag model '''
    class Meta:
        ''' register tag model '''
        model = models.Tag


class Query(graphene.ObjectType):
    ''' register queries '''
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        ''' resolve all posts '''
        return (
          models.Post.objects.prefetch_related("tags")
          .select_related("author")
          .all()
        )

    def resolve_author_by_username(root, info, username):
        ''' resolve author by username '''
        return models.Profile.objects.select_related("user").get(
          user__username=username
        )


    def resolve_post_by_slug(root, info, slug):
        ''' resolve post by slug '''
        return (
          models.Post.objects.prefetch_related("tags")
          .select_related("author")
          .get(slug=slug)
        )


    def resolve_posts_by_author(root, info, username):
        ''' resolve posts by author '''
        return (
          models.Post.objects.prefetch_related("tags")
          .select_related("author")
          .filter(author__user__username=username)
        )


    def resolve_posts_by_tag(root, info, tag):
        ''' resolve posts by tag '''
        return (
          models.Post.objects.prefetch_related("tags")
          .select_related("author")
          .filter(tags__name__iexact=tag)
        )

schema = graphene.Schema(query=Query)
