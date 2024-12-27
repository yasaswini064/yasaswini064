import PyPDF2
from gtts import gTTS

class ConvertPDFAudio:
    def __init__(self, filepath, audiopath):
        self.filepath = filepath
        self.audiopath = audiopath

    def extract_text(self):
        try:
            # Open the PDF file in binary read mode
            with open(self.filepath, 'rb') as pdf_file:
                # Read the PDF using PdfReader
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                
                # Extract text from all pages
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
        except FileNotFoundError:
            print(f"Error: The file '{self.filepath}' was not found.")
            return ""
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
            return ""

    def text_to_audio(self, text):
        try:
            # Convert text to audio
            tts = gTTS(text=text, lang='en')
            tts.save(self.audiopath)
        except Exception as e:
            print(f"Error creating audio file: {e}")

    def pdf_audio(self):
        text = self.extract_text()
        # Check if any text was extracted
        if text.strip():
            self.text_to_audio(text)
            print(f"Audio file saved at: {self.audiopath}")
        else:
            print("No text found in the PDF.")

# Specify the file paths
pdf_file_path = r'C:\Users\SWAROOP\Desktop\process of communication.pdf'  # Your PDF file path
audio_file_path = r'C:\Users\SWAROOP\Desktop\process_of_communication.mp3' # Desired audio output path

# Create an object of the class with the specified file paths
pdf_to_audio = ConvertPDFAudio(pdf_file_path, audio_file_path)

# Call the method to perform the conversion
pdf_to_audio.pdf_audio()
