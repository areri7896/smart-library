import functools
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def track_access(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # Build a readable argument string (skip `self` at index 0)
        positional = ", ".join(repr(a) for a in args[1:])
        keyword = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [positional, keyword]))
        logger.info(
            "ACCESS | method='%s' | args=(%s) | timestamp=%s",
            func.__name__,
            all_args,
            timestamp,
        )
        return func(*args, **kwargs)

    return wrapper


def permission_check(required_role):
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            caller_role = kwargs.get("role", "Guest")
            if caller_role != required_role:
                raise PermissionError(
                    f"Access denied: '{func.__name__}' requires role "
                    f"'{required_role}', but got '{caller_role}'."
                )
            logger.info(
                "PERMISSION | role='%s' granted access to '%s'",
                caller_role,
                func.__name__,
            )
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
