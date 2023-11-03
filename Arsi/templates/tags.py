from django import template
from django.template.loader import render_to_string
from home.models import Social
from service.models import Service
from industry.models import Industry
from solution.models import Solution


register = template.Library()
@register.simple_tag
def header1(request):
    industries = Industry.objects.all()
    services = Service.objects.filter(parent_id=0)
    solutions = Solution.objects.all()
    return render_to_string('sub/header.html', {'industries':industries,'services':services,'solutions':solutions})
@register.simple_tag
def footer(request):
    services = Service.objects.all()
    socials = Social.objects.all()
    return render_to_string('sub/footer.html',{'services':services,'socials':socials,})




