class Logger():

    log_commands = True
    log_results = True

    @staticmethod
    def log_command(command):
        if Logger.log_commands:
            print(f'Executing command: {command}')

    @staticmethod
    def log_result(result):
        if Logger.log_results:
            print(f'Result: {result}')
