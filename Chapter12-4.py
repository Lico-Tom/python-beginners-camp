import threading


class SharedCounter:

    def __init__(self, initial_value=0):
        """
        # a counter object that can be shared by multiple threads.
        """
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        """
        # Increment the counter with Locking
        """
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        """
        # Decrement the counter with Locking
        """
        with self._value_lock:
            self._value -= delta


class SharedCounter_pro:

    def __init__(self, initial_value):
        """
        # A counter object that can be shared by multiple threads.
        """
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        """
        # Increment the counter with Locking
        """
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()

    def decr(self, delta=1):
        """
        # Decrement the counter with Locking
        """
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()

class SharedCounter_plus:
    """
    # A counter object thar can be shared by multiple threads.
    """
    _lock = threading.RLock()

    def __init__(self, initial_value):
        self._value = initial_value

    def incr(self, delta=1):
        """
        # Increment the counter with locking
        """
        with SharedCounter_plus._lock:
            self._value += delta

    def decr(self, delta=1):
        """
        # Decrement the counter with locking
        """
        with SharedCounter_plus._lock:
            self.incr(-delta)
