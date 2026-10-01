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
        ("backend", "Backend Development"),
        ("api", "API Development"),
        ("database", "Database"),
        ("security", "Security"),
        ("devops", "DevOps & Server"),
        ("tools", "Tools"),
        ("testing", "Testing"),
        ("frontend", "Frontend Integration"),
    ]

    name = models.CharField(max_length=80)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="backend"
    )
    icon = models.CharField(
        max_length=60,
        blank=True,
        help_text="Icon CSS class, e.g. devicon-python-plain or fa-solid fa-key",
    )
    level = models.PositiveSmallIntegerField(
        default=80,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="0 se 100 ke beech (ab design me use nahi hota)",
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "sort_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


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

TECH_ICONS = {
    "python": "fa-solid fa-code",
    "django": "devicon-django-plain",
    "drf": "fa-solid fa-layer-group",
    "django rest framework": "fa-solid fa-layer-group",
    "mysql": "fa-solid fa-database",
    "database": "fa-solid fa-database",
    "sql": "fa-solid fa-database",
    "jwt": "fa-solid fa-shield-halved",
    "web development": "fa-solid fa-globe",
    "rest api": "fa-solid fa-link",
    "html": "devicon-html5-plain",
    "css": "devicon-css3-plain",
    "javascript": "devicon-javascript-plain",
    "docker": "devicon-docker-plain",
    "git": "devicon-git-plain",
    "github": "devicon-github-original",
    "linux": "devicon-linux-plain",
}
DEFAULT_TECH_ICON = "fa-solid fa-code"


class Experience(models.Model):
    KIND_CHOICES = [
        ("experience", "Experience"),
        ("education", "Education"),
    ]

    kind = models.CharField(
        max_length=12, choices=KIND_CHOICES, default="experience"
    )
    period = models.CharField(
        max_length=80, help_text="e.g. 2023 - 2026 ya 2026 - Present"
    )
    title = models.CharField(
        max_length=160, help_text="e.g. Python Developer ya Bachelor's Degree"
    )
    organization = models.CharField(
        max_length=160, blank=True, help_text="College / Company name (optional)"
    )
    field = models.CharField(
        max_length=160, blank=True, help_text="e.g. Computer Science / IT (optional)"
    )
    description = models.TextField(blank=True)
    technologies = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated, e.g. Python, Django, DRF, MySQL, JWT",
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return f"{self.title} ({self.period})"

    @property
    def kind_icon(self):
        return (
            "fa-solid fa-graduation-cap"
            if self.kind == "education"
            else "fa-solid fa-briefcase"
        )

    @property
    def tech_list(self):
        return [
            {
                "name": name,
                "icon": TECH_ICONS.get(name.lower(), DEFAULT_TECH_ICON),
            }
            for name in (t.strip() for t in self.technologies.split(","))
            if name
        ]


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