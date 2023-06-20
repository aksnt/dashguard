import os
import shutil
import unittest
from unittest import mock
from main.app import app


class DashboardBackupTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        shutil.rmtree('dashboard_backups', ignore_errors=True)

    def test_backup_dashboards(self):
        response = self.client.get('/backup_dashboards')
        self.assertEqual(response.status_code, 200)

        # Check if dashboard backup files are created
        backup_files = os.listdir('dashboard_backups')
        self.assertGreater(len(backup_files), 0)

    @mock.patch('kibana_api.requests.get')
    def test_export_dashboard(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'objects': [{'id': 'dashboard1', 'data': {...}}]}

        mock_get.return_value = mock_response

        dashboard_data = export_dashboard('dashboard1')
        self.assertIsNotNone(dashboard_data)


if __name__ == '__main__':
    unittest.main()
