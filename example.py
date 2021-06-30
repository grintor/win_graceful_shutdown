import win_graceful_shutdown # this needs to be imported first so that any exit handlers created by modules imported after will surely run
import lovely_logger as log # pip install lovely_logger
import win32con # pip install pywin32
import time
import atexit
import os

log.init('example.log')

def cleanup():

    if win_graceful_shutdown.EXIT_REASON == win32con.CTRL_C_EVENT:
        log.w('got win32con.CTRL_C_EVENT')

    if win_graceful_shutdown.EXIT_REASON == win32con.CTRL_BREAK_EVENT:
        log.w('got win32con.CTRL_BREAK_EVENT')

    if win_graceful_shutdown.EXIT_REASON == win32con.CTRL_CLOSE_EVENT:
        log.w('got win32con.CTRL_CLOSE_EVENT')

    if win_graceful_shutdown.EXIT_REASON == win32con.WM_CLOSE:
        log.w('got win32con.WM_CLOSE')

    if win_graceful_shutdown.EXIT_REASON == win32con.WM_ENDSESSION:
        log.w('got win32con.WM_ENDSESSION')

    for x in range(3):
        log.i('cleaning up...')
        time.sleep(1)

    log.d ("example has ended")

atexit.register(cleanup)


log.d ("example has started")

print('\n')
print(f"Our pid is {os.getpid()}. Try killing it with 'taskkill /pid:{os.getpid()}'")
print('Or try hitting ctrl-c or ctrl-break')
print('Or try closing this window')
print('Or restart this process using pythonw.exe (no console window) and try logging out/rebooting then look in test.log')
print('\n')

while True:
    time.sleep(1)
