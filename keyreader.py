import sys

class KeyReader:
    def __init__(self):
        if sys.platform.startswith('win'):
            self._reader = WindowsKeyReader()
        else:
            self._reader = UnixKeyReader()

    def read(self):
        key = self._reader.read_key()
        return self._handle_key(key)

    def _handle_key(self, key: str) -> str:
        key = key.lower()
        if key in ('1', 'f', 'y', ' '):
            return '1'
        elif key in ('0', 'j', 'n'):
            return '0'
        elif key in ('e', 'q', 'esc'):
            return 'e'
        return '0'  # default fallback


class WindowsKeyReader:
    def __init__(self):
        import msvcrt
        self.msvcrt = msvcrt

    def read_key(self) -> str:
        try:
            while True:
                if self.msvcrt.kbhit():
                    return self.msvcrt.getwch()  # getwch supports unicode
        except KeyboardInterrupt:
            print("\nExiting quiz.")
            sys.exit(0)


class UnixKeyReader:
    def __init__(self):
        import tty, termios
        self.tty = tty
        self.termios = termios

    def read_key(self) -> str:
        fd = sys.stdin.fileno()
        old_settings = self.termios.tcgetattr(fd)
        try:
            self.tty.setraw(fd)
            return sys.stdin.read(1)
        except KeyboardInterrupt:
            print("\nExiting quiz.")
            sys.exit(0)
        finally:
            self.termios.tcsetattr(fd, self.termios.TCSADRAIN, old_settings)