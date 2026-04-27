from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.base import RedirectView


class SiteHomeView(ListView):
    template_name = "home.html"
    context_object_name = "projects"

    def get_queryset(self):
        return []


class PortfolioView(TemplateView):
    template_name = "portfolio.html"

class AboutMeView(TemplateView):
    template_name = "about_me.html"
    
class CVView(TemplateView):
    template_name = "cv.html"
    

# Skills
class SkillsView(RedirectView):
    permanent = True
    pattern_name = "pages:back_end_skills"


class BackEndSkillsView(TemplateView):
    template_name = "skills/back_end.html"


class FrontEndSkillsView(TemplateView):
    template_name = "skills/front_end.html"


class InfrastructureSkillsView(TemplateView):
    template_name = "skills/infrastructure.html"


class SoftwareSkillsView(TemplateView):
    template_name = "skills/software.html"