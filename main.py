from tornado.ioloop import IOLoop
from tornado.web import Application


def create_app():
    return Application(
        [],
        compress_response=True,
    )


PORT = 5000

if __name__ == '__main__':
    application = create_app()
    application.listen(PORT)
    print('a')

    IOLoop.current().start()
