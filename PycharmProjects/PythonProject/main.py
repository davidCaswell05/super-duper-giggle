import curses
# from curses import textpad
curses.initscr()

def auto(stdscr):

    # curses.start_color()
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    # curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
    # curses.init_pair(3, curses.COLOR_RED, curses.COLOR_MAGENTA)

    stdscr.clear()
    curses.echo()
    stdscr.addstr(5, 10, "Do you have any monthly auto expenses? (Y/N): ", curses.color_pair(1))
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == ord('Y'):
            stdscr.clear()
            stdscr.addstr(5, 10,"How much do you spend per month on auto expenses? ", curses.color_pair(2))
            stdscr.refresh()
            amount = stdscr.getstr(6, 10, 10) 
            stdscr.addstr(7, 10, f"This is how much you are spending on auto finances ${amount.decode()}", curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            break
        elif key == ord('N'):
            break
curses.wrapper(auto)

auto()