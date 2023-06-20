import os
import requests

KIBANA_HOST = os.getenv('HOST')


def get_dashboards():
    dashboards_url = f'{KIBANA_HOST}/api/saved_objects/_find?type=dashboard&per_page=10000'
    headers = {'kbn-xsrf': 'true'}
    response = requests.get(dashboards_url, headers=headers)

    if response.status_code == 200:
        return response.json().get('saved_objects', [])
    else:
        return []


def export_dashboard(dashboard_id):
    export_url = f'{KIBANA_HOST}/api/kibana/dashboards/export?dashboard={dashboard_id}'
    headers = {'kbn-xsrf': 'true', 'Content-Type': 'application/json'}
    response = requests.get(export_url, headers=headers)

    if response.status_code == 200:
        return response.json().get('objects', [])
    else:
        return None
