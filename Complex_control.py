import Simple_control as sp

class Complex_control(sp.Simple_control):
    def __init__(self, control_name, error_message, source,control_validation):
        super().__init__(control_name, error_message, source, error_message)
        self.control_validation = control_validation



a= Complex_control()
