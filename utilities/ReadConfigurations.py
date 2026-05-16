import configparser

def read_configurations(basic_info,item):
    config = configparser.ConfigParser()
    config.read('configurations/config.ini')
    return config[basic_info][item]