from tornado.ioloop import IOLoop
from tornado.web import Application

from ci_test.common.constants import ApplicationConstants


def create_app():
    return Application(
        [],
        compress_response=True,
    )


if __name__ == '__main__':
    application = create_app()
    application.listen(ApplicationConstants.PORT)

    IOLoop.current().start()
