import json
import check_on_demand

json_str = """
[
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
"""

if __name__ == '__main__':
    user_file = input()
    bus_dictionary = json.loads(user_file)
    check_on_demand.check_on_demand(bus_dictionary)
