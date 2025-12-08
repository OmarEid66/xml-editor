import sys

class XMLcontroller:
    def format(self, xml_string): 
        tokens = []
        i = 0
        length = len(xml_string)
        
        # Tokenization
        while i < length:
            if xml_string[i] == '<':
                j = xml_string.find('>', i)
                if j == -1: break 
                
                tag = xml_string[i:j+1]
                tokens.append(tag)
                i = j + 1
            else:
                j = i
                while j < length and xml_string[j] != '<':
                    j += 1
                raw_text = xml_string[i:j]
                
                if not raw_text.strip():
                    i = j
                    continue
                tokens.append(raw_text.strip())
                i = j
                
        # Formatting
        formatted = []
        level = 0
        indentation = "    " 
        k = 0
        while k < len(tokens):
            token = tokens[k]
            # Closing Tag 
            if token.startswith('</'):
                level = max(0, level - 1)
                formatted.append((indentation * level) + token) 
            # Opening Tag
            elif token.startswith('<') and not token.startswith('</'):
                # Check for "Leaf Node" (Open -> Text -> Close)
                if (k + 2 < len(tokens) and 
                    not tokens[k+1].startswith('<') and 
                    tokens[k+2].startswith('</') and 
                    len(tokens[k+1]) < 70 and 
                    '\n' not in tokens[k+1]): 
                    
                    line = (indentation * level) + tokens[k] + tokens[k+1] + tokens[k+2]
                    formatted.append(line)
                    k += 2 
                else:
                    formatted.append((indentation * level) + token)
                    level += 1
            # Text Content
            else:
                lines = token.split('\n')
                aligned_lines = []
                for line in lines:
                    stripped_line = line.strip()
                    if stripped_line:
                        aligned_lines.append((indentation * level) + stripped_line)
                formatted.append("\n".join(aligned_lines))
            
            k += 1            
        return "\n".join(formatted)

# --- CLI Logic ---
def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)

def write_file(filepath, content):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Success: Formatted XML saved to '{filepath}'")
    except Exception as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)

def main():
    args = sys.argv
    
    if len(args) < 2:
        print("Usage: python xml_editor.py format -i <input_file> -o <output_file>")
        return

    command = args[1]

    if command == "format":
        # Parse arguments manually using a simple loop (Array Traversal)
        input_file = None
        output_file = None
        
        # Iterate starting from index 2 to find flags
        for idx in range(2, len(args)):
            if args[idx] == "-i" and idx + 1 < len(args):
                input_file = args[idx + 1]
            elif args[idx] == "-o" and idx + 1 < len(args):
                output_file = args[idx + 1]
        
        # Validation
        if not input_file or not output_file:
            print("Error: Missing arguments.")
            print("Usage: python xml_editor.py format -i <input_file> -o <output_file>")
            return

        # Execution Flow
        print(f"Reading from: {input_file}...")
        xml_content = read_file(input_file)
        
        formatter = XMLcontroller()
        formatted_xml = formatter.format(xml_content)
        
        write_file(output_file, formatted_xml)

    else:
        print(f"Unknown command: {command}")
        print("Available commands: format")

if __name__ == "__main__":
    main()