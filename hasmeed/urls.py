"""
URL configuration for hasmeed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from apps.portfolio.views import AboutMeView, BackEndSkillsView, CVView, FrontEndSkillsView, InfrastructureSkillsView, PortfolioView, SiteHomeView, SkillsView, SoftwareSkillsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SiteHomeView.as_view(), name="home"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    path("skills/", SkillsView.as_view(), name="skills"),
    path("skills/back-end/", BackEndSkillsView.as_view(), name="back_end_skills"),
    path("skills/front-end/", FrontEndSkillsView.as_view(), name="front_end_skills"),
    path(
        "skills/infrastructure/", InfrastructureSkillsView.as_view(), name="infrastructure_skills"
    ),
    path("skills/software/", SoftwareSkillsView.as_view(), name="software_skills"),
    path("about-me/", AboutMeView.as_view(), name="about_me"),
    path("cv/", CVView.as_view(), name="cv"),
    path("contact/", include("apps.contact.urls")),
    path("blog/", include("apps.blog.urls")),
]
