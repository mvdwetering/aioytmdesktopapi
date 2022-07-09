"""AioYtmDesktopApi errors."""


class AioYtmDesktopApiException(Exception):
    """Base error for aioytmdesktopapi."""


class RequestError(AioYtmDesktopApiException):
    """
    Unable to fulfill request.
    Raised when host or API cannot be reached.
    """


class Unauthorized(AioYtmDesktopApiException):
    """Application is not authorized."""


def raise_error(code: int, message: str) -> None:
    raise AioYtmDesktopApiException("{}: {}".format(code, message))
