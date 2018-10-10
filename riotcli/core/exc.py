
class RiotCliError(Exception):
    """Generic errors."""

    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return "<RiotCliError - %s>" % self.msg
