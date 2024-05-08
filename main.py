# This Python file uses the following encoding: utf-8
import sys
import os
import asyncio
from datetime import date

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickWindow,QSGRendererInterface
from PySide6.QtQuickControls2 import QQuickStyle


def _init_logger():
    from loguru import logger
    today = date.today()
    logger.add("logs/app{}-{}-{}.log".format(today.year, today.month, today.day), level="INFO", 
        rotation="00:00", compression="zip", encoding="utf-8", retention="30 days", backtrace=True)


async def main(app):

    try:
        future = asyncio.Future()
        _init_logger()

        engine = QQmlApplicationEngine()
        # engine.rootContext().setContextProperty("postMan", post_man)
        QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
        QQuickStyle.setStyle("Fusion")
        engine.addImportPath(os.path.dirname(__file__))
        engine.load(os.path.join(os.path.dirname(__file__), "qml/App.qml"))

        app.aboutToQuit.connect(engine.deleteLater)
        app.aboutToQuit.connect(lambda: os._exit(5))
        engine.quit.connect(app.quit)

        await future
    except Exception as e:
        print(e)
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    import os
    os.environ['QML_IMPORT_TRACE'] = '1'
    os.environ['CONFIG'] = 'qml_debug '

    from PySide6.QtCore import QLockFile, QDir
    import qasync

    lockfile = QLockFile(QDir.tempPath() + '/simulator-1000.lock')

    if lockfile.tryLock(100):
        try:
            app = QApplication()
            loop = qasync.QEventLoop(app)
            asyncio.set_event_loop(loop)
            t = loop.create_task(main(app))
            loop.run_until_complete(t)
            sys.exit(app.exec())
        except Exception as e:
            sys.exit(-1)
    else:
        print("simulator 1000 is already running")
