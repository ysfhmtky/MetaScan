import os
import PyPDF2
import exifread
import pyfiglet

# Function to clear the screen
def clear_screen():
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the banner
def show_banner():
    """Displays the banner with 'MetaScan' in slanted and stylish font."""
    banner = pyfiglet.figlet_format("MetaScan", font="slant")
    neon_blue = "\033[38;5;51m"  # Neon blue color code
    print(neon_blue + banner)
    print(neon_blue + "- By Mr.CodeX\n")

# PDF metadata extraction function
def extract_pdf_metadata(file_path):
    """Extracts metadata from a PDF file."""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            metadata = reader.getDocumentInfo()
            if metadata:
                print("[INFO] PDF Metadata:")
                for key, value in metadata.items():
                    print(f"{key}: {value}")
                print()  # Blank line after metadata
            else:
                print("[INFO] No metadata found.")
    except Exception as e:
        print(f"[ERROR] Failed to extract PDF metadata: {e}")

# Image metadata extraction function (EXIF)
def extract_image_metadata(file_path):
    """Extracts EXIF metadata from an image file."""
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            if tags:
                print("[INFO] Image EXIF Metadata:")
                for tag in tags.keys():
                    print(f"{tag}: {tags[tag]}")
                print()  # Blank line after metadata
            else:
                print("[INFO] No EXIF metadata found.")
    except Exception as e:
        print(f"[ERROR] Failed to extract image metadata: {e}")

# Main function
def main():
    """Main function to run the metadata extraction tool."""
    clear_screen()  # Clear the screen
    show_banner()   # Show the banner
    
    while True:
        print("\nSelect an option:")
        print("1. Extract PDF metadata")
        print("2. Extract image metadata")
        print("3. Exit")
        
        try:
            choice = input("\nEnter your choice (1/2/3): ")
            
            if choice == '1':
                file_path = input("\nEnter the PDF file path: ")
                extract_pdf_metadata(file_path)
                print("\n[INFO] Operation successful. Press Enter to exit...\n")
                input()  # Wait for user to press Enter to exit
                break  # Exit the program after operation
            
            elif choice == '2':
                file_path = input("\nEnter the image file path: ")
                extract_image_metadata(file_path)
                print("\n[INFO] Operation successful. Press Enter to exit...\n")
                input()  # Wait for user to press Enter to exit
                break  # Exit the program after operation
            
            elif choice == '3':
                print("\nExiting...\n")
                break
            
            else:
                print("[ERROR] Invalid choice!\n")

        except KeyboardInterrupt:
            print("\n\n[INFO] Operation interrupted. Exiting...\n")
            break

if __name__ == "__main__":
    main()
