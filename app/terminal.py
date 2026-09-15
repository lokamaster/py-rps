"""Terminal class to print text to terminal, with context manager."""

import sys

# Ansi Escape Sequences
ALT_BUFFER_ON = "\x1b[?1049h"
ALT_BUFFER_OFF = "\x1b[?1049l"
CURSOR_SHOW = "\x1b[?25h"
CURSOR_HIDE = "\x1b[?2hl"
CURSOR_HOME = "\x1b[H"
CLEAR_SCREEN = "\x1b[2J"


class Terminal:
    def __enter__(self):
        # Change to alt buffer and hide cursor
        sys.stdout.write(ALT_BUFFER_ON + CLEAR_SCREEN + CURSOR_HIDE)
        sys.stdout.flush()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore terminal
        sys.stdout.write(CURSOR_SHOW + ALT_BUFFER_OFF)
        sys.stdout.flush()

    def draw(self, frame: str) -> None:
        sys.stdout.write(CURSOR_HOME + CLEAR_SCREEN + frame)
        sys.stdout.flush()
