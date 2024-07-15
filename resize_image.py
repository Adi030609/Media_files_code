from PIL import Image

# Open the image file
with Image.open(r'C:\Users\adity\OneDrive\Desktop\Learning\media_python\red-blue-eyes.jpeg') as img:
    # Resize the image
    img = img.resize((5000, 5000), Image.LANCZOS)
    
    # Convert the image to RGB mode if it is in RGBA mode
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Save it back to disk
    img.save(r'C:\Users\adity\OneDrive\Desktop\Learning\media_python\resized_image.jpg')
