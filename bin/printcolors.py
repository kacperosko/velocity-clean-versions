class PrintColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __print_color(self, color, content):
        print(color + content + self.ENDC)

    def print_success(self, *args, sep=" ") -> None:
        self.__print_color(self.OKGREEN, sep.join(args))

    def print_error(self, *args, sep=" ") -> None:
        self.__print_color(self.FAIL, sep.join(args))

    def print_info(self, *args, sep=" ") -> None:
        self.__print_color(self.OKBLUE, sep.join(args))
