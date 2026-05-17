from django.db import models
from django.urls import reverse


class Project(models.Model):
	class PowerBIEmbedMode(models.TextChoices):
		PUBLIC = "public", "Public link"
		PRIVATE = "private", "Private / secure"

	day_number = models.PositiveSmallIntegerField(unique=True)
	title = models.CharField(max_length=180)
	short_description = models.CharField(max_length=280)
	description = models.TextField()
	problem_statement = models.TextField(blank=True)
	dataset_information = models.TextField(blank=True)
	tools_used = models.TextField(blank=True)
	steps_performed = models.TextField(blank=True)
	insights_discovered = models.TextField(blank=True)
	conclusion = models.TextField(blank=True)
	technologies_used = models.CharField(max_length=260, help_text="Comma separated values.")
	image = models.ImageField(upload_to="projects/", blank=True, null=True)
	github_link = models.URLField(blank=True)
	dashboard_embed_link = models.URLField(blank=True)
	powerbi_report_id = models.CharField(max_length=128, blank=True, help_text="Power BI report ID from the service workspace.")
	powerbi_workspace_id = models.CharField(max_length=128, blank=True, help_text="Power BI workspace/group ID.")
	powerbi_embed_mode = models.CharField(
		max_length=16,
		choices=PowerBIEmbedMode.choices,
		default=PowerBIEmbedMode.PUBLIC,
		help_text="Choose public embedding for publish-to-web or private for secure embed later.",
	)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["day_number"]

	def __str__(self):
		return f"Day {self.day_number}: {self.title}"

	def get_absolute_url(self):
		return reverse("project_detail", kwargs={"day_number": self.day_number})

	@property
	def tech_list(self):
		return [item.strip() for item in self.technologies_used.split(",") if item.strip()]

	@property
	def has_powerbi_metadata(self):
		return bool(self.powerbi_report_id or self.powerbi_workspace_id or self.dashboard_embed_link)
