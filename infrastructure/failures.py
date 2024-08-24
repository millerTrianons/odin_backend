""" Business failuers base class
"""


from typing import Optional


class Failure(Exception):
    """This class represents exceptions of business rules"""

    message = "Generic business rules failure"

    def __init__(self, message: Optional[str] = None):
        if message:
            self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class UnexpectedErrorFailure(Failure):
    """Error class for not expected errors"""

    message = "An unexpected error happened"

    def __init__(self, fromexception: Exception):
        self.message = str(fromexception)
        super().__init__(self.message)
