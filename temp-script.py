import re

def process_line(line):
    # Define the pattern to search for
    pattern = r'confidence interval (\d+\.\d+) for frame window (\d+)'

    # Use regular expression to find matches
    match = re.search(pattern, line)

    if match:
        # Extract values from the match
        confidence_interval = round(float(match.group(1)), 4)
        frame_window = int(match.group(2))

        # Replace the line with the desired format
        return f'{frame_window} {confidence_interval}'
    
    # Return the original line if no match is found
    return line

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            processed_line = process_line(line)
            outfile.write(processed_line + '\n')

if __name__ == "__main__":
    input_file_path = 'temp-output.txt'  # Replace with the path to your input text file
    output_file_path = 'temp-output-processed.txt'  # Replace with the desired output file path

    process_file(input_file_path, output_file_path)