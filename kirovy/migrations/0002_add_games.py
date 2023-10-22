# Generated by Django 4.2.5 on 2023-10-15 16:49
import pathlib

from django.conf import settings
from django.core.files import File
from django.core.files.images import ImageFile

from kirovy import typing as t
from django.db import migrations
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

from kirovy import constants
from kirovy.models import CncGame, CncFileExtension


def _forward(apps: StateApps, schema_editor: DatabaseSchemaEditor):
    mix = CncFileExtension(
        extension="mix",
        extension_type=CncFileExtension.ExtensionTypes.ASSETS.value,
        about="Mix files are uncompressed group files that store game assets.",
    )
    mix.save()
    map_ext = CncFileExtension(
        extension="map",
        extension_type=CncFileExtension.ExtensionTypes.MAP.value,
        about="Map files are ini files that store map data.",
    )
    map_ext.save()
    yrm = CncFileExtension(
        extension="yrm",
        extension_type=CncFileExtension.ExtensionTypes.MAP.value,
        about="Yuri's Revenge custom multiplayer map.",
    )
    yrm.save()
    mpr = CncFileExtension(
        extension="mpr",
        extension_type=CncFileExtension.ExtensionTypes.MAP.value,
        about="RA2 custom multiplayer map.",
    )
    mpr.save()
    mmx = CncFileExtension(
        extension="mmx",
        extension_type=CncFileExtension.ExtensionTypes.MAP.value,
        about="Mix file containing a .MAP file and a .PKT file.",
    )
    mmx.save()
    yro = CncFileExtension(
        extension="yro",
        extension_type=CncFileExtension.ExtensionTypes.MAP.value,
        about="Mix file containing a .MAP file and a .PKT file.",
    )
    yro.save()

    yr_extensions = (mix, map_ext, mpr, mmx, yrm, yro)

    tib_dawn = CncGame.objects.create(
        slug="td",
        full_name=f"{constants.cnc_prefix} Tiberian Dawn",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=None,
        is_mod=False,
    )
    tib_dawn.save()
    tib_dawn.allowed_extensions.add(mix, map_ext)

    red_alert = CncGame.objects.create(
        slug="ra",
        full_name=f"{constants.cnc_prefix} Red Alert",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=None,
        is_mod=False,
    )
    red_alert.save()
    red_alert.allowed_extensions.add(mix, map_ext)

    dune_2k = CncGame.objects.create(
        slug="d2k",
        full_name="Dune 2000",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=None,
        is_mod=False,
    )
    dune_2k.save()
    dune_2k.allowed_extensions.add(mix, map_ext)

    tib_sun = CncGame.objects.create(
        slug="ts",
        full_name=f"{constants.cnc_prefix} Tiberian Sun",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=None,
        is_mod=False,
    )
    tib_sun.save()
    tib_sun.allowed_extensions.add(mix, map_ext)

    red_alert_2 = CncGame.objects.create(
        slug="ra2",
        full_name=f"{constants.cnc_prefix} Red Alert 2",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=None,
        is_mod=False,
    )
    red_alert_2.save()
    red_alert_2.allowed_extensions.add(mix, map_ext, mpr, mmx)

    yuri = CncGame.objects.create(
        slug="yr",
        full_name=f"{constants.cnc_prefix} Red Alert 2: Yuri's Revenge",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=red_alert_2,
        is_mod=False,
        compatible_with_parent_maps=True,
    )
    yuri.save()
    yuri.allowed_extensions.add(*yr_extensions)

    dta = CncGame.objects.create(
        slug="dta",
        full_name="Dawn of The Tiberium Age",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=tib_sun,
        is_mod=True,
    )
    dta.save()
    dta.allowed_extensions.add(mix, map_ext)

    mental_omega = CncGame.objects.create(
        slug="mo",
        full_name="Mental Omega",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=yuri,
        is_mod=True,
    )
    mental_omega.save()
    mental_omega.allowed_extensions.add(*yr_extensions)

    twisted_insurrection = CncGame.objects.create(
        slug="ti",
        full_name="Twisted Insurrection",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=tib_sun,
        is_mod=True,
    )
    twisted_insurrection.save()
    twisted_insurrection.allowed_extensions.add(mix, map_ext)

    red_resurrection = CncGame.objects.create(
        slug="rr",
        full_name="YR Red-Resurrection",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=yuri,
        is_mod=True,
    )
    red_resurrection.save()
    red_resurrection.allowed_extensions.add(*yr_extensions)

    cnc_reloaded = CncGame.objects.create(
        slug="cncr",
        full_name="C&C Reloaded",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=yuri,
        is_mod=True,
    )
    cnc_reloaded.save()
    cnc_reloaded.allowed_extensions.add(*yr_extensions)

    rise_of_the_east = CncGame.objects.create(
        slug="rote",
        full_name="Rise Of The East",
        is_visible=True,
        allow_public_uploads=False,
        parent_game=yuri,
        is_mod=True,
    )
    rise_of_the_east.save()
    rise_of_the_east.allowed_extensions.add(*yr_extensions)


def _backward(apps: StateApps, schema_editor: DatabaseSchemaEditor):
    """Deleting the games on accident could be devastating to the db so no."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("kirovy", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(_forward, reverse_code=_backward),
    ]
