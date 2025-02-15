import threading
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

# Create a receiver function
@receiver(my_signal)
def my_handler(sender, **kwargs):
    print(f"Handler thread: {threading.current_thread().name}")

# Send the signal
print(f"Caller thread: {threading.current_thread().name}")
my_signal.send(sender=None)