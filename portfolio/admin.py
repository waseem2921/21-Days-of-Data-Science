from django.contrib import admin
from django.utils.html import format_html

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("day_number", "title", "preview_technologies", "date_created")
	list_filter = ("date_created",)
	search_fields = ("title", "short_description", "description", "technologies_used")
	ordering = ("day_number",)

	def preview_technologies(self, obj):
		technologies = obj.tech_list[:4]
		return format_html("<span>{}</span>", ", ".join(technologies))

	preview_technologies.short_description = "Technologies"
