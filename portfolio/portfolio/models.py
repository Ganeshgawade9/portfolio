from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)


class SiteProfile(models.Model):
    name = models.CharField(max_length=120, default="Your Name")
    role = models.CharField(max_length=120, default="Web Developer")
    summary = models.TextField(
        default="I create clean, modern, and useful digital experiences."
    )
    email = models.EmailField(default="hello@yourname.com")
    phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=120, blank=True)

    portrait = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf"]
            )
        ],
        help_text="Upload your resume as a PDF file.",
    )

    available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name


class AboutCard(models.Model):
    icon = models.CharField(
        max_length=10,
        default="👨‍💻",
        help_text="Emoji shown top-left of the card"
    )
    title = models.CharField(
        max_length=80,
        help_text="e.g. Who I Am, What I Do, Education, My Goal"
    )
    content = models.TextField(
        help_text="Short 2-4 sentence blurb"
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return f"{self.icon} — {self.title}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("database", "Database"),
        ("tools", "Tools"),
    ]

    name = models.CharField(max_length=80)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="backend"
    )
    level = models.PositiveSmallIntegerField(
        default=80,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="0 se 100 ke beech",
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "sort_order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=160)
    short_description = models.TextField()
    case_study = models.TextField(blank=True)
    technologies = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated technologies"
    )
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [
            item.strip()
            for item in self.technologies.split(",")
            if item.strip()
        ]


class Experience(models.Model):
    period = models.CharField(max_length=80)
    title = models.CharField(max_length=160)
    description = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("linkedin", "LinkedIn"),
        ("instagram", "Instagram"),
        ("hackerrank", "HackerRank"),
        ("github", "GitHub"),
        ("other", "Other"),
    ]

    label = models.CharField(
        max_length=50,
        help_text="Text shown on the site, e.g. LinkedIn"
    )
    url = models.URLField(
        help_text="Full profile link, starting with https://"
    )
    icon = models.CharField(
        max_length=30,
        choices=PLATFORM_CHOICES,
        default="other",
        verbose_name="Platform",
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return self.label


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"