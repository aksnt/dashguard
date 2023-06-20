from flask import Flask, jsonify
from backup_service import backup_dashboards

app = Flask(__name__)


@app.route('/backup_dashboards')
def backup():
    message = backup_dashboards()
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run()
