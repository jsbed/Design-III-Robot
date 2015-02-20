from PySide.QtGui import QTextCursor


class Outputer():

    def __init__(self, widget):
        self._TextBrowser = widget

    def output(self, newOutput):
        if (newOutput):
            cleanOutput = self._cleanOutput(newOutput)
            self._TextBrowser.append(cleanOutput)
            self._TextBrowser.moveCursor(QTextCursor.End)

    def clearOutput(self):
        self._TextBrowser.setPlainText("")

    def _cleanOutput(self, output):
        return output.replace("\n", "").replace("\r", "")
