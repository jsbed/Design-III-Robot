class Deplacement():

    def __init__(self, ui, tcp_client):
        self._ui = ui
        self._tcp_client = tcp_client
        self._setup_ui()

    def _setup_ui(self):
        self._ui.up_button.clicked.connect(self._up_arrow)
        self._ui.down_button.clicked.connect(self._down_arrow)
        self._ui.left_button.clicked.connect(self._left_arrow)
        self._ui.right_button.clicked.connect(self._right_arrow)
        self._ui.rotate_right_button.clicked.connect(self._rotate_right_arrow)
        self._ui.rotate_left_button.clicked.connect(self._rotate_left_arrow)

    def _up_arrow(self):
        if self._ui.move_line_edit.text():
            self._tcp_client.send_data("move-up-" +
                                       self._ui.move_line_edit.text())

    def _down_arrow(self):
        if self._ui.move_line_edit.text():
            self._tcp_client.send_data("move-down-" +
                                       self._ui.move_line_edit.text())

    def _left_arrow(self):
        if self._ui.move_line_edit.text():
            self._tcp_client.send_data("move-left-" +
                                       self._ui.move_line_edit.text())

    def _right_arrow(self):
        if self._ui.move_line_edit.text():
            self._tcp_client.send_data("move-right-" +
                                       self._ui.move_line_edit.text())

    def _rotate_right_arrow(self):
        if self._ui.rotate_line_edit.text():
            self._tcp_client.send_data("rotate-right-" +
                                       self._ui.rotate_line_edit.text())

    def _rotate_left_arrow(self):
        if self._ui.rotate_line_edit.text():
            self._tcp_client.send_data("rotate-left-" +
                                       self._ui.rotate_line_edit.text())
