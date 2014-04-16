def make_log(level):
    def _(message):
        print("{}: {}".format(level, message))
    return _

log_info = make_log("info")
log_warning = make_log("warning")
log_error = make_log("error")