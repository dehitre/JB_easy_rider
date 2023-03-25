from check_list import Checks


def get_errors(bus_dictionary):
    """
    get errors for all kind of info and then call print
    :param bus_dictionary: timetable in json
    """
    bus_id_error = check_bus_id(bus_dictionary)
    stop_id_error = check_stop_id(bus_dictionary)
    stop_name_error = check_stop_name(bus_dictionary)
    next_stop_error = check_next_stop(bus_dictionary)
    next_stop_type_error = check_next_stop_type(bus_dictionary)
    arrive_type_error = check_arrive_time(bus_dictionary)
    print_result(bus_id_error, stop_id_error, stop_name_error, next_stop_error, next_stop_type_error, arrive_type_error)


def get_stop_count(bus_dictionary):
    """
    get all stops for each line and then call print
    :param bus_dictionary:
    """
    stops_in_line = get_stops_in_line(bus_dictionary)
    print_bus_stop_count(stops_in_line)


def check_bus_id(bus_dict):
    """
    check if bus id is correct for each point in timetable    :param bus_dict: in json
    :return: errors number
    """
    error_count = 0
    bus_id = "bus_id"
    for i in bus_dict:
        if not Checks.check_existance(bus_id, i):
            error_count += 1
        else:
            if not Checks.check_int(i[bus_id]):
                error_count += 1
            else:
                if not Checks.check_int_existance(i[bus_id]):
                    error_count += 1
                else:
                    pass
    return error_count


def check_stop_id(bus_dict):
    """
    check if stop id is correct for each point in timetable    :param bus_dict: in json
    :return: errors number
    """
    error_count = 0
    stop_id = "stop_id"
    for i in bus_dict:
        if not Checks.check_existance(stop_id, i):
            error_count += 1
        else:
            if not Checks.check_int(i[stop_id]):
                error_count += 1
            else:
                if not Checks.check_int_existance(i[stop_id]):
                    error_count += 1
                else:
                    pass
    return error_count


def check_stop_name(bus_dict):
    """
    check if stop name is correct for each point in timetable    :param bus_dict: in json
    :return: errors number
    """
    error_count = 0
    stop_name = "stop_name"
    for i in bus_dict:
        if not Checks.check_existance(stop_name, i):
            error_count += 1
        elif not Checks.check_str(i[stop_name]):
            error_count += 1
        elif not Checks.check_empty_string(i[stop_name]):
            error_count += 1
        elif not Checks.check_bus_stop_proper_name(i[stop_name]):
            error_count += 1
        else:
            pass
    return error_count


def check_next_stop(bus_dict):
    """
    check if next stop is correct for each point in timetable    :param bus_dict: in json
    :return: errors number
    """
    error_count = 0
    next_stop = "next_stop"
    for i in bus_dict:
        if not Checks.check_existance(next_stop, i):
            error_count += 1
        else:
            if not Checks.check_int(i[next_stop]):
                error_count += 1
            else:
                if not Checks.check_int_existance(i[next_stop]):
                    error_count += 1
                else:
                    pass
    return error_count


def check_next_stop_type(bus_dict):
    """
    check if next stop type is correct for each point in timetable    :param bus_dict: in json
    :return: errors number
    """
    error_count = 0
    next_stop_type = "stop_type"
    for i in bus_dict:
        if Checks.check_existance(next_stop_type, i):
            if not Checks.check_stop_type(i[next_stop_type]):
                error_count += 1
    return error_count


def check_arrive_time(bus_dict):
    """
    check if arrive time is correct for each point in timetable    :param bus_dict: in json
    :return: errors number
    """
    error_count = 0
    a_time = "a_time"
    for i in bus_dict:
        if not Checks.check_existance(a_time, i):
            error_count += 1
        elif not Checks.check_str(i[a_time]):
            error_count += 1
        elif not Checks.check_empty_string(i[a_time]):
            error_count += 1
        elif not Checks.check_date_format(i[a_time]):
            error_count += 1
        else:
            pass
    return error_count


def get_stops_in_line(bus_dict):
    """
    get all stops for each line
    :param bus_dict: json
    :return: dictionary bus line: [stops]
    """
    bus_stop_dict = {}
    bus_id = "bus_id"
    for i in bus_dict:
        bus_num = i[bus_id]
        if bus_num in bus_stop_dict.keys():
            bus_stop_dict[bus_num] += 1
        else:
            bus_stop_dict[bus_num] = 1
    return bus_stop_dict


def print_result(bus_id_error, stop_id_error, stop_name_error, next_stop_error, next_stop_type_error,
                 arrive_type_error):
    """
    print errors in timetable
    :param bus_id_error: int
    :param stop_id_error:int
    :param stop_name_error:int
    :param next_stop_error:int
    :param next_stop_type_error:int
    :param arrive_type_error:int
    """
    sum = bus_id_error + stop_id_error + stop_name_error + next_stop_type_error + next_stop_error + arrive_type_error
    print(f"Format validation: {sum} errors")
    print(f"""stop_name: {stop_name_error}
stop_type: {next_stop_type_error}
a_time: {arrive_type_error}
    """)


def print_bus_stop_count(stops_in_line):
    """
    print stops for each bus line
    :param stops_in_line:
    """
    print("Line names and number of stops:")
    for key, val in stops_in_line.items():
        print(f"bus_id: {key}, stops: {val}")
