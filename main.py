from pyscript import display, document

def check_temperature(e):
    document.getElementById("output").innerHTML = ""  # Clear previous output

    fahrenheit = float(document.getElementById("fahrenheit").value)

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9

    # Display Celsius temperature
    display(f"Temperature in Celsius: {float(celsius)}", target="output")

    # Fever check
    if celsius >= 37.8:
        display("Fever detected.", target="output")
    else:
        display("No fever.", target="output")
