import win_graceful_shutdown
import win32con # pip install pywin32
import time
import atexit
import os
from datetime import datetime

def log(msg):
    print(f"LOG: {msg}")
    with open("example.log", "a") as f:
        f.write(f"{msg}\n")

def cleanup():
    if win_graceful_shutdown.EXIT_REASON == win32con.CTRL_C_EVENT:
        log('got win32con.CTRL_C_EVENT')

    if win_graceful_shutdown.EXIT_REASON == win32con.CTRL_BREAK_EVENT:
        log('got win32con.CTRL_BREAK_EVENT')

    if win_graceful_shutdown.EXIT_REASON == win32con.CTRL_CLOSE_EVENT:
        log('got win32con.CTRL_CLOSE_EVENT')

    if win_graceful_shutdown.EXIT_REASON == win32con.WM_CLOSE:
        log('got win32con.WM_CLOSE')

    if win_graceful_shutdown.EXIT_REASON == win32con.WM_ENDSESSION:
        log('got win32con.WM_ENDSESSION')

    for x in range(7):
        log('cleaning up...')
        time.sleep(1)

    log (f"{os.path.basename(__file__)} has ended at {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")

atexit.register(cleanup)

log (f"{os.path.basename(__file__)} has started at {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")

print('\n')
print(f"Our pid is {os.getpid()}. Try killing it with 'taskkill /pid:{os.getpid()}'")
print('Or try hitting ctrl-c or ctrl-break')
print('Or try closing this window')
print('Or restart this process using pythonw.exe (no console window) and try logging out/rebooting then look in test.log')
print('\n')

while True:
    time.sleep(1)
