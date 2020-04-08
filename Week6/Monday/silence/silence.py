def silence(map_path):

    def real_silence(func):

        def wrapper_silence(*args):
            try:
                func(*args)
            except Exception as err:
                with open(map_path, 'a') as file:
                    file.write("{} raise an error - {} \n".format(func.__name__, str(err)))
            return func(*args)
        return wrapper_silence
    return real_silence
