from django import template
from ..models import Comment  # Import your models

register = template.Library()

@register.inclusion_tag('pages/comment.html')
def render_comments(comment, depth=0):
    replies = Comment.objects.filter(parent_comment=comment)
    return {'comment': comment, 'replies': replies, 'depth': depth}
