🔳 Simple Python QR Code GeneratorThis project is a lightweight Python script for generating QR codes from any text or URL input. It's built for simplicity and uses the widely adopted qrcode library.✨ FeaturesGenerate QR Codes: Easily create a QR code from a string of text or a URL.Save as Image: Outputs the generated QR code directly to a high-quality PNG image file.Customizable: Simple to modify the input data directly within the Python file.🚀 Setup and InstallationPrerequisitesYou must have Python 3.x installed on your system.1. Install DependenciesThis project only requires the official qrcode library, which also relies on Pillow for image handling.pip install qrcode[pil]
2. UsageSave the code (e.g., as qr_generator.py).Open the file (qr_generator.py) in your text editor.Locate the line defining the data you want to encode (it will look something like this):data = "[https://www.google.com](https://www.google.com)" # <--- EDIT THIS LINE
Change the text inside the quotes ("...") to your desired URL or message.Run the script from your terminal:python qr_generator.py
OutputAfter running the script, a new file named qrcode_output.png will be created in the same directory, containing your generated QR code.⚙️ Core Code SnippetThe generation process is handled by just a few lines of code:import qrcode

# 1. Define the data to be encoded
data = "Hello World! This is a test QR Code."

# 2. Create the QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 3. Add data and compile the image
qr.add_data(data)
qr.make(fit=True)

# 4. Create the final image and save it
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_output.png")

print(f"QR code successfully generated and saved as qrcode_output.png")
