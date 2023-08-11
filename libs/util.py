""" Python script with utility functions """
def strNoneConvert(input_data):
    """ Converting input to string if it is not a list or none """
    if input_data is None:
        return None
    return list if input_data is list else str(input_data)


def floatNoneConvert(input_data):
    """ Converting input to float if it is not a list or none """
    if input_data is None or input_data == '':
        return None
    return list if input_data is list else float(input_data)


def otherinputtodict(input_data):

    """ Dict [parser funtion for other inputs """
    input_parameter_dict = {}
    if input_data is not None:
        if "=" in input_data:
            input_parameter_list = input_data.split(",")
            for parameter in input_parameter_list:
                input_parameter_dict[parameter.split(
                    "=")[0]] = parameter.split("=")[1]

    return input_parameter_dict
