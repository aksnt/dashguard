import os
from kibana_api import get_dashboards, export_dashboard

BACKUP_DIRECTORY = 'dashboard_backups'


def backup_dashboards():
    # Create backup directory if it doesn't exist
    if not os.path.exists(BACKUP_DIRECTORY):
        os.makedirs(BACKUP_DIRECTORY)

    dashboards = get_dashboards()

    for dashboard in dashboards:
        dashboard_id = dashboard.get('id')
        dashboard_title = dashboard.get('attributes', {}).get('title')
        dashboard_filename = f'{dashboard_id}_{dashboard_title}.json'

        dashboard_data = export_dashboard(dashboard_id)

        if dashboard_data:
            with open(os.path.join(BACKUP_DIRECTORY, dashboard_filename), 'w') as f:
                f.write(dashboard_data)
        else:
            return f'Failed to export dashboard: {dashboard_title}'

    return 'Dashboards backup completed'
