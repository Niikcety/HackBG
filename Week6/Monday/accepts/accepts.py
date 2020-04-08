def accepts(*decorator_args):

    def real_accepts(function):

        def accepts_wrapper(*wrapper_args):
            if len(decorator_args) != len(wrapper_args):
                raise ValueError('Different size of arguments')
            for i in range(len(wrapper_args)):
                if not isinstance(wrapper_args[i], decorator_args[i]):
                    raise TypeError("Argument \"{}\" of {} is not {}".format(wrapper_args[i], function.__name__, decorator_args[i]))
            return function(*wrapper_args)
        return accepts_wrapper

    return real_accepts
