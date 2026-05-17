from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Project


def home(request):
	query = request.GET.get("q", "").strip()
	technology_filter = request.GET.get("technology", "").strip()

	projects = Project.objects.all()
	if query:
		projects = projects.filter(
			Q(title__icontains=query)
			| Q(short_description__icontains=query)
			| Q(description__icontains=query)
			| Q(technologies_used__icontains=query)
		)

	if technology_filter:
		projects = projects.filter(technologies_used__icontains=technology_filter)

	all_technologies = sorted(
		{
			technology
			for project in Project.objects.all()
			for technology in project.tech_list
		}
	)

	total_projects = Project.objects.count()
	total_technologies = len(all_technologies)

	context = {
		"projects": projects,
		"query": query,
		"technology_filter": technology_filter,
		"all_technologies": all_technologies,
		"stats": {
			"projects": total_projects,
			"technologies": total_technologies,
			"hours": max(total_projects, 21) * 3,
		},
	}
	return render(request, "portfolio/home.html", context)


def project_detail(request, day_number):
	project = get_object_or_404(Project, day_number=day_number)
	return render(request, "portfolio/project_detail.html", {"project": project})
