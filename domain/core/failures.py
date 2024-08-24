from infrastructure.failures import Failure


class ParametersNotFound(Failure):

    def __init__(self):
        message = "Parameters Not Found"
        super().__init__(message)