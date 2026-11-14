"""A small, dependency-free example for practicing with Copilot."""


def greeting(name: str = "learner") -> str:
    """Return a friendly greeting for a non-empty name."""
    clean_name = name.strip() or "learner"
    return f"Hello, {clean_name}! Welcome to Copilot Skills Lab."


if __name__ == "__main__":
    print(greeting())
