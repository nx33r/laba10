import logging

class RedundantChargeException(Exception):
    pass

def logged(exception, mode):
    def decorator(func):
        def wrapper(self):
            try:
                return func(self)
            except exception as e:
                logging.basicConfig(filename='log.txt', level=logging.INFO)
                if mode == 'console':
                    logging.info(str(e))
                    print(f"Logged exception: {e}")
                elif mode == 'file':
                    logging.info(str(e))
                else:
                    raise ValueError("Invalid logging mode")
        return wrapper
    return decorator

class AbstractPhone:
    def charge(self):
        raise NotImplementedError("charge() method must be implemented in subclasses")

class MyPhone(AbstractPhone):
    @logged(RedundantChargeException, mode='console')
    def charge(self):
        battery_level = 100
        if battery_level == 100:
            raise RedundantChargeException("The phone battery is already fully charged")
        else:
            print("Charging the phone...")

phone = MyPhone()
phone.charge()

