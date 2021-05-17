# win_graceful_shutdown
A python library for handling graceful shutdown in response to:
  CTRL_C_EVENT,
  CTRL_BREAK_EVENT,
  CTRL_CLOSE_EVENT,
  WM_CLOSE,
  and WM_ENDSESSION

Python has built-in support for exit handlers though the [atexit](https://docs.python.org/3/library/atexit.html) standard library. The problem is, it's pretty hard to get those exit handlers to run relibaly on windows. The windows console might close your program via CTRL_C_EVENT or CTRL_BREAK_EVENT, and those are pretty easy to catch and handle. But It might also close your program via CTRL_CLOSE_EVENT, which is a bit more complicated to handle, but not much. Where it startes to get hary trying to handle WM_CLOSE, which is what taskkill sends, or WM_ENDSESSION which is what windows sends when it is shutting down.

This handles all of those situations with a simple import. Simply import win_graceful_shutdown and your exit handlers are guaranteed to fire when the progam closes.
