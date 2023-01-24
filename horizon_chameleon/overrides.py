import horizon
from django.conf import settings

projects_dashboard = horizon.get_dashboard("project")
# Security groups only work on KVM sites, so we will hide them on bare metal sites.
security_groups_panel = projects_dashboard.get_panel("security_groups")
if not settings.CHAMELEON_SITE_ID.startswith("KVM"):
    projects_dashboard.unregister(security_groups_panel.__class__)
