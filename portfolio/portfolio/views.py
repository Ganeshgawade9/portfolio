from django.contrib import messages
from django.shortcuts import redirect, render
from .models import AboutCard, ContactMessage, Experience, Project, SiteProfile, Skill, SocialLink

def home(request):
    profile = SiteProfile.objects.first() or SiteProfile()
    context = {
        "profile": profile,
        "about_cards": AboutCard.objects.all(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.filter(featured=True),
        "experience": Experience.objects.all(),
        "social_links": SocialLink.objects.all(),
    }
    if request.method == "POST":
        ContactMessage.objects.create(name=request.POST.get("name", ""), email=request.POST.get("email", ""), message=request.POST.get("message", ""))
        messages.success(request, "Thanks — your message was sent.")
        return redirect("home")
    return render(request, "portfolio/home.html", context)