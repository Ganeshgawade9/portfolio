import time

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import (
    AboutCard,
    Experience,
    Project,
    SiteProfile,
    Skill,
    SocialLink,
)


def home(request):
    profile = SiteProfile.objects.first() or SiteProfile()

    if request.method == "POST":
        form = ContactForm(request.POST)
        last_sent = request.session.get("last_contact", 0)

        if time.time() - last_sent < 30:
            messages.error(request, "Please wait a few seconds before sending another message.")
        elif form.is_valid():
            contact = form.save()
            request.session["last_contact"] = time.time()

            if profile.email:
                send_mail(
                    subject=f"New portfolio message from {contact.name}",
                    message=f"{contact.message}\n\nReply to: {contact.email}",
                    from_email=None,
                    recipient_list=[profile.email],
                    fail_silently=True,
                )

            messages.success(request, "Thanks — your message was sent.")
            return redirect(reverse("home") + "#contact")
    else:
        form = ContactForm()

    context = {
        "profile": profile,
        "form": form,
        "about_cards": AboutCard.objects.all(),
        "skills": Skill.objects.order_by("category", "sort_order", "name"),
        "projects": Project.objects.filter(featured=True),
        "experience": Experience.objects.all(),
        "social_links": SocialLink.objects.all(),
    }
    return render(request, "portfolio/home.html", context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    profile = SiteProfile.objects.first() or SiteProfile()
    return render(
        request,
        "portfolio/project_detail.html",
        {"project": project, "profile": profile},
    )