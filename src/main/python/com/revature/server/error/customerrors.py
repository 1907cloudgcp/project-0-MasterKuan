class Error(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, account, amount, message):
        self.account = account
        self.amount = amount
        self.message = message

    def formatted_message(self):
        return "Message: {0}, Account: #{1}, Amount: ${2:.2f}".format(self.message, self.account, self.amount)


class LargeDeposit(Error):
    pass


class LargeWithdrawal(Error):
    pass
