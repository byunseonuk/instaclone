from django import template
import re

register = template.Library()

@register.filter
def add_link(value):
    #print(dir(value))
    content = value.content
    tags = value.tag_set.all()
    #print(dir(tags))
    for tag in tags:
        print(tag)
        content = re.sub(r'\#'+tag.name+r'\b', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content)
    return content
