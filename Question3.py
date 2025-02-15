from django.db import transaction, models
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

# Create a receiver function
@receiver(my_signal)
def my_handler(sender, **kwargs):
    print("Handler executed within transaction")

# Send the signal within a transaction
with transaction.atomic():
    print("Before sending signal")
    my_signal.send(sender=None)
    print("After sending signal")