import time
from plyer import notification  # Correctly importing just 'notification'

while True:
    # Show the notification
    notification.notify(
        title="💧 Reminder",
        message="Drink some water!",
        timeout=10  # How long the notification stays visible
    )

    time.sleep(10)  # Wait for 10 seconds before showing next reminder
