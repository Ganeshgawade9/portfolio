# Generated manually to add the missing AboutCard table

from django.db import migrations, models


def seed_about_cards(apps, schema_editor):
    AboutCard = apps.get_model('portfolio', 'AboutCard')
    if AboutCard.objects.exists():
        return
    AboutCard.objects.bulk_create([
        AboutCard(
            number="01",
            icon="👨‍💻",
            title="Who I Am",
            content="I'm Ganesh Gawade, a Python Full Stack Developer who loves turning ideas into clean, working products.",
            sort_order=1,
        ),
        AboutCard(
            number="02",
            icon="⚙️",
            title="What I Do",
            content="Backend Development, Frontend Development, and everything needed to ship a complete web application.",
            sort_order=2,
        ),
        AboutCard(
            number="03",
            icon="🎓",
            title="Education",
            content="Master's Degree in Computer Applications, with a strong foundation in programming and software design.",
            sort_order=3,
        ),
        AboutCard(
            number="04",
            icon="🎯",
            title="My Goal",
            content="To grow as a Python/Django developer and build impactful, real-world web applications.",
            sort_order=4,
        ),
    ])


def remove_about_cards(apps, schema_editor):
    AboutCard = apps.get_model('portfolio', 'AboutCard')
    AboutCard.objects.filter(title__in=["Who I Am", "What I Do", "Education", "My Goal"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_siteprofile_about_education_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='01', help_text='e.g. 01, 02, 03, 04', max_length=4)),
                ('icon', models.CharField(default='👨\u200d💻', help_text='Emoji shown top-left of the card', max_length=10)),
                ('title', models.CharField(help_text='e.g. Who I Am, What I Do, Education, My Goal', max_length=80)),
                ('content', models.TextField(help_text='Short 2-4 sentence blurb')),
                ('sort_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.RunPython(seed_about_cards, remove_about_cards),
    ]