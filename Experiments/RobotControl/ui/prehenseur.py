class Prehenseur():

    def __init__(self, ui, tcp_client):
        self._ui = ui
        self._tcp_client = tcp_client
        self._setup_ui()

    def _setup_ui(self):
        self._ui.take_cube_button.clicked.connect(self._take_cube)
        self._ui.drop_cube_button.clicked.connect(self._drop_cube)
        self._ui.open_gripper_max_button.clicked.connect(self._open_gripper)
        self._ui.lift_gripper_button.clicked.connect(self._lift_gripper)
        self._ui.lower_gripper_button.clicked.connect(self._lower_gripper)

    def _take_cube(self):
        self._tcp_client.send_data("take_cube")

    def _drop_cube(self):
        self._tcp_client.send_data("drop cube")

    def _open_gripper(self):
        self._tcp_client.send_data("open gripper")

    def _lift_gripper(self):
        self._tcp_client.send_data("lift gripper")

    def _lower_gripper(self):
        self._tcp_client.send_data("lower gripper")
