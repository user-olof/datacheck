class DataTypeMismatchError(Exception):
    """ Data type mismatch between arg and control input """


class XXX:
"""

:return

"""
    @staticmethod
    def compare(arg, control_data):
        try:
            datacheck = _DataCheck.setup(arg, control_data)
            res = datacheck.check_instances()
            return res
        except Exception as ex:
            print(ex)


class _DataCheck:
    """
    Instantiate a data check operation.
    Object and control data are both compared by type and by value

    :param obj: Data object in the code
    :type obj: Any
    :param control_data: Control data used for testing
    :type control_data: Any
    """

    def __init__(self, obj, control_data):
        self.obj = obj
        self.control_data = control_data
        self.all_types_verified = []
        self.all_values_verified = []

    @classmethod
    def setup(cls, obj, control_data):
        return _DataCheck(obj, control_data)

    def check_type(self, arg, control_data, /):
        """
        Check that type of arg and control data is matching
        :param arg: Data object in the code.
        :type arg: Any
        :param control_data: Control data used for testing.
        :type: control_data: Any
        :return: Object type
        """
        # arg needs to equal contol_input
        # both in type and data
        if type(arg) == type(control_data):
            return type(arg)
        else:
            raise DataTypeMismatchError



    def traverse(self, obj, /):
        """
        :param obj: It uses recursion on obj to investigate the data types.
        :type obj: Any
        :return: The inner data item. Ends recursion when it has found the value.
        """
        if isinstance(obj, list | tuple):
            for value in obj:
                for subvalue in self.traverse(value):
                    yield subvalue
        elif isinstance(obj, dict):
            for key in obj.keys():
                for subvalue in self.traverse(obj[key]):
                    yield subvalue
        # here we can add more data types
        else:
            yield obj

    def check_instances(self):
        """
        :return list of validated data types. The list is only
        generated if all data types are valid, otherwise an
        exception is thrown
        """
        try:
            # retrieve information
            arg_list = list(self.traverse(self.obj))
            control_data_list = list(self.traverse(self.control_data))

            # check and determine size
            size = -1
            if len(arg_list) == len(control_data_list):
                size = len(arg_list)
            else:
                raise DataTypeMismatchError("Size of arg does not match size of control input")

            # check type and value
            i = 0
            while i < size:
                t = self.check_type(arg_list[i], control_data_list[i])
                self.all_types_verified.append(t)
                if arg_list[i] == control_data_list[i]:
                    val = arg_list[i]
                else:
                    val = DataTypeMismatchError("Arg: " + str(arg_list[i]) + " || Control data: " + str(control_data_list[i]))
                self.all_values_verified.append(val)
                i += 1

            return self.all_types_verified, self.all_values_verified

        except DataTypeMismatchError as ex:
            print('\n' + str(ex))
        except Exception as ex:
            print(ex)
