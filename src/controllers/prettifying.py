class XMLFormatter:
    def format(self, xml_string):
        xml_string = xml_string.replace('\n', '').strip()
        
        # Tokenize
        tokens = []
        i = 0
        length = len(xml_string)
        
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
                text = xml_string[i:j].strip()
                if text:
                    tokens.append(text)
                i = j

        formatted_lines = []
        indent_level = 0
        indent_str = "    " 
        
        k = 0
        while k < len(tokens):
            token = tokens[k]
            
            # Closing Tag 
            if token.startswith('</'):
                indent_level = max(0, indent_level - 1)
                formatted_lines.append((indent_str * indent_level) + token)
                
            # Opening Tag
            elif token.startswith('<') and not token.startswith('</'):
                if (k + 2 < len(tokens) and 
                    not tokens[k+1].startswith('<') and 
                    tokens[k+2].startswith('</')):      
                    
                    line = (indent_str * indent_level) + tokens[k] + tokens[k+1] + tokens[k+2]
                    formatted_lines.append(line)
                    k += 2 
                    
                else:
                    formatted_lines.append((indent_str * indent_level) + token)
                    indent_level += 1
            
            # Text Content (for long text or mixed content)
            else:
                formatted_lines.append((indent_str * indent_level) + token)
            
            k += 1
            
        return "\n".join(formatted_lines)

# Testing the Code
input_xml = """<?xml version="1.0" encoding="UTF-8"?>
<users>
<user>
<id>1</id>
<name>Ahmed Ali</name>
<posts>
<post>
<body>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</body>
<topics>
<topic>
economy"""
formatter = XMLFormatter()
output = formatter.format(input_xml)
print(output)