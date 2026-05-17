from django.contrib import admin
from django.utils.html import format_html

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("day_number", "title", "powerbi_embed_mode", "preview_technologies", "date_created")
	list_filter = ("date_created", "powerbi_embed_mode")
	search_fields = (
		"title",
		"short_description",
		"description",
		"technologies_used",
		"powerbi_report_id",
		"powerbi_workspace_id",
	)
	ordering = ("day_number",)
	fieldsets = (
		(
			"Project Content",
			{
				"fields": (
					"day_number",
					"title",
					"short_description",
					"description",
					"problem_statement",
					"dataset_information",
					"tools_used",
					"steps_performed",
					"insights_discovered",
					"conclusion",
					"technologies_used",
					"image",
					"github_link",
				),
			}
		),
		(
			"Power BI Metadata",
			{
				"fields": (
					"dashboard_embed_link",
					"powerbi_embed_mode",
					"powerbi_report_id",
					"powerbi_workspace_id",
				),
			}
		),
	)

	def preview_technologies(self, obj):
		technologies = obj.tech_list[:4]
		return format_html("<span>{}</span>", ", ".join(technologies))

	preview_technologies.short_description = "Technologies"
