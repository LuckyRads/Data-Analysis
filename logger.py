class Logger():

    should_log_commands = True
    should_log_results = True
    should_log_infos = True

    @staticmethod
    def log_command(command):
        if Logger.should_log_commands:
            print(f'Command: {command}')

    @staticmethod
    def log_info(info):
        if Logger.should_log_infos:
            print(f'Info: {info}')

    @staticmethod
    def log_result(result):
        if Logger.should_log_results:
            print(f'Result: {result}')

    @staticmethod
    def log_error(error):
        print(f'Error: {error}')
