from pydoc import locate
from typing import Tuple, Callable

from flask import Flask, Blueprint


def add_commands(app: Flask, commands: Tuple) -> None:
    if not commands:
        return None

    for command_name, command_container_reference, decorators in commands:
        app.cli.command(command_name)(
            __decorate_command_callable(decorators, __get_command_callable(command_container_reference))
        )


def __get_command_callable(command_container_reference) -> Callable:
    cli = locate(command_container_reference)
    command_callable = lambda *args, **kwargs: cli()(*args, **kwargs)  # noqa
    command_callable.__name__ = command_container_reference
    return command_callable


def __decorate_command_callable(decorators, command_callable) -> Callable:
    if not decorators:
        return command_callable

    decorated_callable = command_callable
    for callable_decorator in reversed(decorators):
        decorated_callable = callable_decorator(decorated_callable)

    return decorated_callable
