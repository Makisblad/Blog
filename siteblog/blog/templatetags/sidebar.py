from django import template
from blog.models import *


register = template.Library()

@register.inclusion_tag('blog/popular_posts.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by("-viwes")[:cnt]
    return {'posts': posts}

@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
