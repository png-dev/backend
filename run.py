from flask_cors import CORS
from application.app import create_app
if __name__ == '__main__':
    app = create_app()
    CORS(app, resources={r"/v1/*": {"origins": "*"}})

    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )
