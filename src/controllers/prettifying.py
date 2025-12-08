class XMLcontroller:
    def format(self, xml_string): 
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
                raw_text = xml_string[i:j]
                
                if not raw_text.strip():
                    i = j
                    continue
                tokens.append(raw_text.strip())
                i = j
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
                if (k + 2 < len(tokens) and 
                    not tokens[k+1].startswith('<') and 
                    tokens[k+2].startswith('</') and len(tokens[k+1]) < 70 and '\n' not in tokens[k+1]): 
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
# --- Test ---
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
economy
</topic>
<topic>
finance
</topic>
</topics>
</post>
<post>
<body>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</body>
<topics>
<topic>
solar_energy
</topic>
</topics>
</post>
</posts>
<followers>
<follower>
<id>2</id>
</follower>
<follower>
<id>3</id>
</follower>
</followers>
<followings>
<following>
<id>2</id>
</following>
<following>
<id>3</id>
</following>
</followings>
</user>
<user>
<id>2</id>
<name>Yasser Ahmed</name>
<posts>
<post>
<body>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</body>
<topics>
<topic>
education
</topic>
</topics>
</post>
</posts>
<followers>
<follower>
<id>1</id>
</follower>
</followers>
<followings>
<following>
<id>1</id>
</following>
</followings>
</user>
<user>
<id>3</id>
<name>Mohamed Sherif</name>
<posts>
<post>
<body>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</body>
<topics>
<topic>
sports
</topic>
</topics>
</post>
</posts>
<followers>
<follower>
<id>1</id>
</follower>
</followers>
<followings>
<following>
<id>1</id>
</following>
</followings>
</user>
</users>"""
formatter = XMLcontroller()
print(formatter.format(input_xml))