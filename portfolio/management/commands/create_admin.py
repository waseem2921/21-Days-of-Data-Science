import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a superuser from environment variables (non-interactive)."

    def handle(self, *args, **options):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME")
        email = os.getenv("ADMIN_EMAIL", "")
        password = os.getenv("ADMIN_PASSWORD")

        if not username or not password:
            self.stdout.write(self.style.ERROR("Environment variables ADMIN_USERNAME and ADMIN_PASSWORD must be set."))
            return

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        if created:
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created superuser: {username}"))
            return

        # Update existing user to be staff/superuser and ensure password
        changed = False
        if not user.is_staff:
            user.is_staff = True
            changed = True
        if not user.is_superuser:
            user.is_superuser = True
            changed = True
        user.set_password(password)
        user.save()
        msg = "Updated" if changed else "Password set for"
        self.stdout.write(self.style.SUCCESS(f"{msg} superuser: {username}"))
