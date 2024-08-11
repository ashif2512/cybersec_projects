import subprocess

def get_last_word_of_each_line(file_path):
    try:
        with open(file_path, 'r') as file:
            last_words = []
            for line in file:
                # Strip any leading/trailing whitespace
                line = line.strip()
                
                # Split the line by backslash and get the last part
                if line:
                    last_word = line.split('\\')[-1]
                    last_words.append(last_word)
            return last_words
    
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

# Use a raw string for the file path to handle backslashes correctly
def main():
    
    file_path = r"C:\python\get_software.txt"

    try:
        result = subprocess.run(["reg", "query", "HKLM\\software\\"], capture_output=True, text=True)
        with open(file_path, 'w') as file:
            file.write(result.stdout)

    except Exception as e:
        print(f"An error occured while running the reg command '{e}'")
        return
    
    last_words = get_last_word_of_each_line(file_path)

    if last_words:
        print("Available software name:")
        for word in last_words:
            print(word)

if __name__ == '__main__':
    main()




