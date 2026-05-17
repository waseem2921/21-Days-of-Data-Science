from django.core.management.base import BaseCommand

from portfolio.models import Project


PROJECT_TITLES = [
    "Global Data Analysis",
    "AI Trend Prediction",
    "Netflix Data Visualization",
    "Sales Forecasting with Time Series",
    "Customer Churn Analysis",
    "House Price Prediction",
    "Sentiment Analysis from Social Media",
    "Loan Risk Classification",
    "HR Attrition Insights",
    "E-Commerce Recommendation Basics",
    "COVID-19 Impact Storyboard",
    "Retail Basket Analysis",
    "Fraud Detection Signals",
    "Stock Market Volatility Snapshot",
    "Power BI Executive Dashboard",
    "SQL Analytics Challenge",
    "Python Automation for Reporting",
    "Data Cleaning Marathon",
    "Clustering Customer Segments",
    "A/B Testing Outcome Analysis",
    "Capstone: End-to-End Analytics Case",
]

TECH_STACKS = [
    "Python, Pandas, Matplotlib, SQL",
    "Python, Scikit-learn, NumPy, AI",
    "Python, Pandas, Seaborn, Visualization",
    "Python, Prophet, Time Series, Analytics",
    "Python, Pandas, ML, Classification",
    "Python, Regression, Scikit-learn, Statistics",
    "Python, NLP, AI, Text Analytics",
    "Python, ML, SQL, Risk Modeling",
    "Python, Power BI, HR Analytics, Pandas",
    "Python, Recommendation, SQL, Analytics",
    "Python, Data Storytelling, Plotly, Analytics",
    "Python, Apriori, Analytics, Retail",
    "Python, Anomaly Detection, ML, Finance",
    "Python, Time Series, Finance, Visualization",
    "Power BI, DAX, SQL, Dashboarding",
    "SQL, Python, Analytics, Database",
    "Python, Automation, Pandas, Reporting",
    "Python, Data Cleaning, Pandas, ETL",
    "Python, Clustering, Scikit-learn, ML",
    "Python, Experimentation, Statistics, Analytics",
    "Python, SQL, Power BI, ML",
]


class Command(BaseCommand):
    help = "Seed Day 1 to Day 21 portfolio projects."

    def handle(self, *args, **options):
        created_count = 0
        for index, title in enumerate(PROJECT_TITLES, start=1):
            project, created = Project.objects.update_or_create(
                day_number=index,
                defaults={
                    "title": title,
                    "short_description": f"Day {index} project focused on real-world data science and analytics outcomes.",
                    "description": (
                        f"This project explores practical data science concepts on Day {index}. "
                        "The workflow demonstrates data cleaning, exploratory analysis, model experimentation, and communication of results."
                    ),
                    "problem_statement": "Define a measurable business problem and identify the key metric to optimize.",
                    "dataset_information": "Public dataset with mixed numerical and categorical fields, prepared for analysis.",
                    "tools_used": "Python notebooks, SQL queries, visualization tools, and dashboarding environment.",
                    "steps_performed": "Data collection, preprocessing, EDA, feature engineering, modeling, and evaluation.",
                    "insights_discovered": "Detected strong feature relationships and actionable patterns for stakeholder decisions.",
                    "conclusion": "Project delivered clear insights and a repeatable process for future data initiatives.",
                    "technologies_used": TECH_STACKS[index - 1],
                    "github_link": "https://github.com/",
                    "dashboard_embed_link": "",
                },
            )
            if created:
                created_count += 1
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action}: Day {project.day_number} - {project.title}"))

        self.stdout.write(self.style.WARNING(f"Total newly created projects: {created_count}"))
