from .base import Command

class IssueResolver:
    def __init__(self, command: Command):
        self.command = command

    def resolve(self):
        return self.command.execute()
