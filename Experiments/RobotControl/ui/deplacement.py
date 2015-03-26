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
        self._tcp_client.send_data("up")

    def _down_arrow(self):
        self._tcp_client.send_data("down")

    def _left_arrow(self):
        self._tcp_client.send_data("left")

    def _right_arrow(self):
        self._tcp_client.send_data("right")

    def _rotate_right_arrow(self):
        self._tcp_client.send_data("rotate-right")

    def _rotate_left_arrow(self):
        self._tcp_client.send_data("rotate-left")
