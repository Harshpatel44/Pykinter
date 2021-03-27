def singleton(my_class):
    instances = {}

    def get_instance(*args, **kwargs):
        if my_class not in instances:
            instances[my_class] = my_class(*args, **kwargs)
        return instances[my_class]

    return get_instance
