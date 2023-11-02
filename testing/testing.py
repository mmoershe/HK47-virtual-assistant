import subprocess

def get_raspberry_pi_temperature():
    result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
    print(result)
    return result.stdout.strip()

print(f"Heat levels: {get_raspberry_pi_temperature()}")