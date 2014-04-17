def make_log(level):
    def _(message):
        print("%s: %s" % (level, message))
    return _

log_info = make_log("info")
log_warning = make_log("warning")
log_error = make_log("error")

log_info("Hello")
log_warning("Hello")
log_error("Hello")

def make_counter():
    i = 0
    def _():
        nonlocal i # This line is new
        i += 1
        return i
    return _