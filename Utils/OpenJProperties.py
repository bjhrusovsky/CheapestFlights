from jproperties import Properties


def openFile(fileName: str) -> Properties:
    configs = Properties()
    with open(f'{fileName}', 'rb') as config_file:
        configs.load(config_file)
    return configs