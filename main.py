from tornado.ioloop import IOLoop
from tornado.web import Application


def create_app():
    return Application(
        [],
        compress_response=True,
    )


if __name__ == '__main__':
    application = create_app()
    application.listen(5000)
    print('a')

    IOLoop.current().start()
