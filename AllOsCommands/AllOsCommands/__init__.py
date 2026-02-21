"""PEP 8-friendly import path for the package.

This module re-exports the public API from the legacy `AllOsCommands` package
so users can do:

    import all_os_commands
    from all_os_commands import clearOnAllUI, is_enter_pressed
"""

from AllOsCommands import clearOnAllUI, is_enter_pressed

__all__ = ["clearOnAllUI", "is_enter_pressed"]
