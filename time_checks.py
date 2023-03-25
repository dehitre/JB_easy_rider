def check_time_increasing(bus_number, bus_dict):
    """
    check that time increasing for stops for one line
    :param bus_number: bus line
    :param bus_dict: timetable
    :return: stop name of error time or False if there is no error
    """
    st_hours = 0
    st_minutes = 0
    for bus in bus_dict:
        if bus["bus_id"] == bus_number:
            hour, minute = bus["a_time"].split(":")
            hour = int(hour)
            minute = int(minute)
            if hour > st_hours:
                st_hours = hour
                st_minutes = minute
            elif minute > st_minutes:
                st_minutes = minute
            else:
                return bus["stop_name"]
    return False


def print_no_problem():
    """
    print if all stops have correct time
    """
    print("Arrival time test:")
    print("OK")


def print_problem_stops(timetable_problems):
    """
    print stops with incorrect time
    :param timetable_problems: dictionary bus line: name of stop
    """
    print("Arrival time test:")
    for k, v in timetable_problems.items():
        print(f"bus_id line {k}: wrong time on station {v}")


def check_time(bus_dict):
    """
    check that all stops have correct time and call print
    :param bus_dict:
    """
    bus_array = []
    timetable_problems = {}
    for bus in bus_dict:
        bus_number = bus["bus_id"]
        if bus_number not in bus_array:
            stop_name = check_time_increasing(bus_number, bus_dict)
            if stop_name:
                timetable_problems[bus_number] = stop_name
            bus_array.append(bus_number)
    if timetable_problems == {}:
        print_no_problem()
    else:
        print_problem_stops(timetable_problems)
