#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate

# Optional: create/update admin during deploy when explicitly enabled.
if [ "${CREATE_ADMIN_ON_DEPLOY:-false}" = "true" ]; then
	if [ -n "${ADMIN_USERNAME:-}" ] && [ -n "${ADMIN_PASSWORD:-}" ]; then
		python manage.py create_admin
	else
		echo "CREATE_ADMIN_ON_DEPLOY=true but ADMIN_USERNAME/ADMIN_PASSWORD are missing; skipping admin creation."
	fi
fi

python manage.py collectstatic --no-input
