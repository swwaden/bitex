# Import Built-Ins
import logging

# Import Third-Party

# Import Homebrew

# Init Logging Facilities
log = logging.getLogger(__name__)


class IncompleteCredentialsWarning(UserWarning):
    pass

class IncompleteCredentialConfigurationWarning(UserWarning):
    pass

class IncompleteCredentialsError(Exception):
    pass

class IncompleteAPIConfigurationWarning(UserWarning):
    pass
