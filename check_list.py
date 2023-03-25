import re


class Checks:
    @staticmethod
    def check_existance(k_id, obj):
        if k_id in obj.keys():
            return True
        else:
            return False

    @staticmethod
    def check_int(val):
        """
        check if id is int
        :param val: id
        :return: True or False
        """
        if isinstance(val, int):
            return True
        else:
            return False

    @staticmethod
    def check_int_existance(val):
        """
        check if id is empty
        :param val: id
        :return: True or False
        """
        if val >= 0:
            return True
        else:
            return False

    @staticmethod
    def check_empty_string(val):
        if len(val) == 0:
            return False
        else:
            return True

    @staticmethod
    def check_bus_stop_proper_name(val):
        """
        check that stop has name ended "Street", "Avenue", "Boulevard", "Road" and all words start with capital letter
        :param val: stop namr
        :return: True or False
        """
        street_array = val.split(" ")
        if street_array[-1] not in ["Street", "Avenue", "Boulevard", "Road"] or len(street_array) < 2:
            return False
        for i in street_array:
            if not i[0].isupper():
                return False
        return True

    @staticmethod
    def check_stop_type(val):
        """
        check that stop has correct type
        :param val: stop type
        :return: True or False
        """
        if val in ["S", "O", "F", ""]:
            return True
        else:
            return False

    @staticmethod
    def check_str(val):
        """
        check that name is a string
        :param val: name
        :return: True or False
        """
        if type(val) == str:
            return True
        else:
            return False

    @staticmethod
    def check_date_format(val):
        """
        check that time is in correct format
        :param val: time
        :return: True or False
        """
        if re.match("[0-2][0-9]:[0-5][0-9]$", val):
            hour, minute = val.split(":")
            if 0 <= int(hour) < 24 and 0 <= int(minute) < 60:
                return True
        else:
            return False
