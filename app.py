import os

from applications import create_app

app = create_app()


if __name__ == '__main__':
    # app.run()
    app.run(host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=os.getenv('FLASK_RUN_PORT', '9001'))
