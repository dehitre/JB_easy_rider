def find_stop_start(bus, bus_dict):
    """
    find final, start and all stops for line
    :param bus: timetable in json
    :param bus_dict:  bus line
    :return: find final, start and all stops, if final or start stop is empty return False
    """
    start_stop = ""
    final_stop = ""
    stops_array = []
    for i in bus_dict:
        if i["bus_id"] == bus and i["stop_type"] == "S":
            stops_array.append(i["stop_name"])
            start_stop = i["stop_name"]
        elif i["bus_id"] == bus and i["stop_type"] == "F":
            stops_array.append(i["stop_name"])
            final_stop = i["stop_name"]
        elif i["bus_id"] == bus:
            stops_array.append(i["stop_name"])
        else:
            pass
    if start_stop != "" and final_stop != "":
        return start_stop, final_stop, stops_array
    else:
        return False


def print_stop_error(bus):
    """
    print error in case if final or start stop is empty return False
    :param bus: bus number
    """
    print(f"There is no start or end stop for the line: {bus}.")


def check_stop_and_start_for_buses(bus_dict):
    """
    check if final and start presents and call prine
    :param bus_dict: timetable in json
    :return: False if there is at least one error, otherwise True
    """
    bus_array = []
    for bus in bus_dict:
        bus_number = bus["bus_id"]
        if bus_number not in bus_array:
            if not find_stop_start(bus_number, bus_dict):
                print_stop_error(bus_number)
                return False
            else:
                bus_array.append(bus_number)
    return True


def find_intersections(bus_array, inter_stop):
    """
    find intersections that are transfer stops
    :param bus_array: bus lines numbers
    :param inter_stop: stops
    :return: set of transfer stops
    """
    lst = set()
    i = 0
    j = i+1
    while i <= len(bus_array)-2:
        while j <= len(bus_array)-1:
            for n in inter_stop[bus_array[i]]:
                if n in inter_stop[bus_array[j]]:
                    lst.add(n)
            j += 1
        i += 1
        j = i + 1
    return lst


def print_stops_result(start_stops,intersection_stops,final_stops):
    """
    print all kind of stops
    :param start_stops: start stops
    :param intersection_stops: transfer stops
    :param final_stops: finish stops
    """
    start_stops = sorted(list(start_stops))
    intersection_stops = sorted(list(intersection_stops))
    final_stops = sorted(list(final_stops))
    print(f"Start stops: {len(start_stops)} {start_stops}")
    print(f"Transfer stops: {len(intersection_stops)} {intersection_stops}")
    print(f"Finish stops: {len(final_stops)} {final_stops}")


def check_all_stops(bus_dict):
    """
    check all stops
    :param bus_dict:
    """
    bus_array = []
    start_stops = set()
    final_stops = set()
    inter_stop = {}
    for bus in bus_dict:
        bus_number = bus["bus_id"]
        if bus_number not in bus_array:
            start, final, all = find_stop_start(bus_number, bus_dict)
            start_stops.add(start)
            final_stops.add(final)
            inter_stop[bus_number] = list(set(all))
            bus_array.append(bus_number)
    intersection_stops = find_intersections(bus_array, inter_stop)
    print_stops_result(start_stops,intersection_stops,final_stops)


