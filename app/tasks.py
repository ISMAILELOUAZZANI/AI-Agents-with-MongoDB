# Define task schemas, validation, and utilities here
def validate_task(task):
    if not isinstance(task, str) or not task:
        raise ValueError("Task must be a non-empty string.")
    return True