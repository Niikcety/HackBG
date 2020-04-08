import time


def performance(file_path):
    start_time = time.time()

    def real_performance(function):

        def wrapper_performance(*args):
            with open(file_path, 'a') as file:
                file.write("{} was called and took {} to complete\n".format(function.__name__, round(time.time() - start_time, 2)))
            file.close()
            print()
            return function(*args)
        return wrapper_performance
    return real_performance


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return 'I\'m done'


print(something_heavy())
print(something_heavy())
