from abc import ABC, abstractmethod


class ApiResponse(ABC):

    def __init__(self, status_code):
        self.status_code = status_code
