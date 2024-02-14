# Generated by Django 4.2.5 on 2024-02-14 04:50

from django.db import migrations
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps
from django.utils.text import slugify

from kirovy import typing as t
from kirovy.models import MapCategory as _MapCategory, CncUser as _User


def _forward(apps: StateApps, schema_editor: DatabaseSchemaEditor):

    # This is necessary in case later migrations make schema changes to this model.
    # Importing them normally will use the latest schema state and will crash if those
    # migrations are after this one.
    MapCategory: t.Type[_MapCategory] = apps.get_model("kirovy", "MapCategory")
    CncUser: t.Type[_User] = apps.get_model("kirovy", "CncUser")

    migration_user = CncUser.objects.get_or_create_migration_user()

    yuri_category_names = {
        "Battle",
        "YR Ladder",
        "RA2 Ladder",
        "RA2 Pro 2v2",
        "Free For All",
        "Cooperative",
        "Naval War",
        "Unholy Alliance",
        "Megawealth",
        "Meat Grinder",
        "Team Alliance",
        "Land Rush",
        "Mod Maps",
        "Standard",
        "SFJ",
        "Blitz",
        "Survival",
    }

    for category_name in yuri_category_names:
        # Note: Custom overriden .save() doesn't work in migrations, so
        # we have to manually make the slug.
        category = MapCategory(
            name=category_name,
            slug=slugify(category_name),
            last_modified_by=migration_user,
        )
        category.save()


def _backward(apps: StateApps, schema_editor: DatabaseSchemaEditor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("kirovy", "0002_add_games"),
    ]

    # Elidable=false means that squashmigrations will not delete this.
    operations = [
        migrations.RunPython(_forward, reverse_code=_backward, elidable=False),
    ]
