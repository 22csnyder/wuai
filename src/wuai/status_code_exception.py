import time

class StatusCodeException(Exception):
    def __init__(self, status_code, response):
        self.status_code = status_code
        self.response = response
        super().__init__(self._generate_message())

    def _generate_message(self):
        if self.status_code == 401:
            error_message = self.response.json().get("message", "")
            if "Access Token is missing or invalid" in error_message:
                return "Token expired. Fetching a new token..."
            return "Unauthorized access. Please check your credentials."
        elif self.status_code == 403:
            return (
                "Response is a 403 error code. You may be receiving this error code if you are not on WashU's network or VPN."
            )
        elif self.status_code == 402:
            return (
                "Response is a 402 error code. You may be receiving this error code if you have exceeded the budget of your account. "
                "Please contact di2accelerator@wustl.edu for assistance."
            )
        elif self.status_code == 418:
            return (
                "Response is a 418 error code. You may be receiving this error code if more than 10 calls a second have been performed. "
                "Please contact di2accelerator@wustl.edu for assistance."
            )
        else:
            return self.response.text

class TimeoutException(Exception):
    pass

class Timeout:
    def __init__(self, seconds):
        self.seconds = seconds

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        if elapsed_time > self.seconds:
            raise TimeoutException(f"Operation exceeded {self.seconds} seconds timeout.")