import stops_in_line


def find_stops_on_demand(bus_dict):
    """
    find the list of all on-demand stops
    :param bus_dict: all  stops
    :return: list on-demand stops
    """
    stops = set()
    for bus in bus_dict:
        if bus["stop_type"] == "O":
            stops.add(bus["stop_name"])
    return stops


def print_result(on_demand_stops, non_demand_stops):
    """
    print result if there are on-demand stops in terminal, start or termination stops or not
    :param on_demand_stops: list of all on-demand stops
    :param non_demand_stops: list of stops that cannot be on-demand
    """
    res_arr = []
    on_demand_stops = list(on_demand_stops)
    non_demand_stops = list(non_demand_stops)
    for i in on_demand_stops:
        if i in non_demand_stops:
            res_arr.append(i)
    res_arr.sort()
    print("On demand stops test:")
    if len(res_arr) > 0:
        print(f"Wrong stop type: {res_arr}")
    else:
        print("OK")


def check_on_demand(bus_dict):
    """
    get list on-demand stops and list of stops that cannot be on-demand
    after print result
    :param bus_dict: dictionary with all stops
    """
    bus_array = []
    start_stops = set()
    final_stops = set()
    inter_stop = {}
    for bus in bus_dict:
        bus_number = bus["bus_id"]
        if bus_number not in bus_array:
            start, final, all = stops_in_line.find_stop_start(bus_number, bus_dict)
            start_stops.add(start)
            final_stops.add(final)
            inter_stop[bus_number] = list(set(all))
            bus_array.append(bus_number)
    intersection_stops = stops_in_line.find_intersections(bus_array, inter_stop)
    on_demand_stops = find_stops_on_demand(bus_dict)
    non_demand_stops = start_stops.union(final_stops)
    non_demand_stops.update(intersection_stops)
    print_result(on_demand_stops, non_demand_stops)
