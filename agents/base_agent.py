"""Base agent abstractions."""

class BaseAgent:
    def __init__(self, name="base"):
        self.name = name

    def act(self, observation):
        raise NotImplementedError
