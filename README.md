## Kibana Dashboard Backup

This script allows you to back up all existing dashboards in Kibana using the ELK API. The backup files are saved as separate JSON files, which can be imported to restore the dashboards in case of any issues or data loss.

## Prerequisites

- Python 3.6 or above
- Flask
- Requests

## Installation

1. Clone this repository or download the code files.
2. Install the required dependencies using pip:

```bash
pip install flask requests
```

### Configuration
3. Open the kibana_api.py file and modify the KIBANA_HOST variable to the URL of your Kibana instance. For example: 

```python
HOST=http://localhost:5601
```

### Usage
Start the Flask application by running the app.py file:

```bash
python app.py
```

The Flask application will start running on http://localhost:5000.

Trigger the backup process by making a GET request to http://localhost:5000/backup_dashboards 

```bash
curl http://localhost:5000/backup_dashboards
```

The script will retrieve the existing dashboards from the Kibana instance, export each dashboard individually, and save them as separate JSON files in the dashboard_backups directory. 

Once the backup process is completed, the backup files will be available in the dashboard_backups directory.