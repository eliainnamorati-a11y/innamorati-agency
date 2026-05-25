import json

transcript_path = "/Users/eliainnamorati/.gemini/antigravity/brain/23d5bc53-f00a-4ab0-9427-69f0f6290637/.system_generated/logs/transcript.jsonl"

with open(transcript_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'VIEW_FILE' and '<!-- Team Section (Nordex Focal Row Style) -->' in data.get('content', ''):
            content = data['content']
            # Find the start
            start_str = '<!-- Team Section (Nordex Focal Row Style) -->'
            start_idx = content.find(start_str)
            
            # Since view_file has line numbers like "184:   <!-- Team Section", we can use regex to strip line numbers later
            # For now, let's just grab the block and we will clean it.
            
            import re
            # Extract lines from content
            lines = content.split('\n')
            team_lines = []
            in_team = False
            for l in lines:
                if '<!-- Team Section (Nordex Focal Row Style) -->' in l:
                    in_team = True
                
                if in_team:
                    # strip the line number prefix (e.g. "185:   ")
                    cleaned = re.sub(r'^\d+:\s', '', l)
                    team_lines.append(cleaned)
                    
                    if 'id="insights-scroll-section"' in l or '<!-- Awards Section -->' in l:
                        # Reached the next section
                        team_lines.pop() # remove the line that triggered the end
                        break
                        
            if team_lines:
                # the last line might be </section> or something, let's just write it
                with open('team_section_recovered.html', 'w') as out:
                    out.write('\n'.join(team_lines))
                print("Recovered!")
                break
