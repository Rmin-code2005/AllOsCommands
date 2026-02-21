import os
import sys
def clearOnAllUI():
    os.system("cls" if os.name == "nt" else "clear")
def is_enter_pressed() -> bool:

    if os.name == "nt":
        # ویندوز
        import msvcrt
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch in (b'\r', b'\n'):
                # Enter رو مصرف می‌کنیم
                return True
        return False

    else:
        # لینوکس / macOS
        import select
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)
            rlist, _, _ = select.select([sys.stdin], [], [], 0)
            if rlist:
                ch = sys.stdin.read(1)
                if ch in ('\r', '\n'):
                    return True
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return False