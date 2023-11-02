import subprocess

def get_raspberry_pi_temperature():
    result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
    temperature_string = result.stdout.strip()
    temperature = float(temperature_string.split('=')[1].split("'")[0])
    return temperature

# Example usage
temperature = get_raspberry_pi_temperature()
print(f"The temperature of the Raspberry Pi is {temperature} degrees Celsius.")
