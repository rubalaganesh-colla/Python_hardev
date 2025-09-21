import os
def shutdown_computer():
    """
    This function shuts down the computer.
    """
    try:
        os.system("shutdown /s /t 1")
        print("Shutdown initiated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
shutdown_computer()
