# Generated by Django 4.1.7 on 2023-02-25 23:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import students.helpers


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                ("title", models.TextField(verbose_name="Title")),
                ("message", models.TextField(verbose_name="Message")),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.CreateModel(
            name="Major",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                ("name", models.TextField(verbose_name="Name")),
                ("price", models.PositiveBigIntegerField(verbose_name="Price")),
                ("description", models.TextField(verbose_name="Description")),
            ],
            options={
                "verbose_name": "Major",
                "verbose_name_plural": "Majors",
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                ("name", models.TextField(verbose_name="Name")),
            ],
            options={
                "verbose_name": "Region",
                "verbose_name_plural": "Regions",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "contract_type",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "B"), (2, "BG"), (3, "M"), (4, "MG")],
                        verbose_name="Contact Type",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Name")),
                ("surname", models.CharField(max_length=30, verbose_name="Surname")),
                (
                    "middle_name",
                    models.CharField(max_length=30, verbose_name="Middle Name"),
                ),
                ("birth_of_date", models.DateField(verbose_name="Birth Of Date")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("address", models.TextField(verbose_name="Address")),
                ("phone", models.CharField(max_length=17, verbose_name="Phone")),
                (
                    "passport_series",
                    models.CharField(max_length=2, verbose_name="Passport Series"),
                ),
                (
                    "passport_number",
                    models.CharField(max_length=7, verbose_name="Passport Number"),
                ),
                ("PIN", models.CharField(max_length=14, verbose_name="PIN")),
                ("authority", models.TextField(verbose_name="Authority")),
                (
                    "gender",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Man"), (2, "Female")], verbose_name="Gender"
                    ),
                ),
                ("discount", models.BooleanField(verbose_name="Discount")),
                (
                    "percent",
                    models.FloatField(blank=True, null=True, verbose_name="Percent"),
                ),
                (
                    "discount_from",
                    models.DateField(
                        blank=True, null=True, verbose_name="Discount From"
                    ),
                ),
                (
                    "discount_to",
                    models.DateField(blank=True, null=True, verbose_name="Discount To"),
                ),
                ("super_contract", models.BooleanField(verbose_name="Super Contract")),
                (
                    "super_contract_sum",
                    models.PositiveBigIntegerField(
                        blank=True, null=True, verbose_name="Super Contract Sum"
                    ),
                ),
                (
                    "passport_document",
                    models.FileField(
                        upload_to=students.helpers.FilePaths.get_passport_document_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf", "heif", "hevc"]
                            )
                        ],
                        verbose_name="Passport Document",
                    ),
                ),
                (
                    "IELTS_document",
                    models.FileField(
                        upload_to=students.helpers.FilePaths.get_IELTS_document_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf", "heif", "hevc"]
                            )
                        ],
                        verbose_name="IELTS Document",
                    ),
                ),
                (
                    "contract_document",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=students.helpers.FilePaths.get_contract_document_path,
                        verbose_name="Contract Document",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Recently Added"),
                            (2, "For consideration from marketing admin"),
                            (3, "For consideration from rector admin"),
                            (4, "Accepted"),
                            (5, "Not accepted"),
                            (6, "Deleted"),
                        ],
                        default=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "comments",
                    models.ManyToManyField(
                        blank=True, to="students.comment", verbose_name="Comments"
                    ),
                ),
                (
                    "major",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="students.major",
                        verbose_name="Major",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="students.region",
                        verbose_name="Region",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
        ),
    ]
