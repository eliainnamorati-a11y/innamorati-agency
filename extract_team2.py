import json, re

transcript_path = "/Users/eliainnamorati/.gemini/antigravity/brain/23d5bc53-f00a-4ab0-9427-69f0f6290637/.system_generated/logs/transcript.jsonl"
with open(transcript_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'VIEW_FILE' and '<!-- Team Section' in data.get('content', ''):
            content = data['content']
            lines = content.split('\n')
            
            in_team = False
            team_lines = []
            
            for l in lines:
                if '<!-- Team Section' in l:
                    in_team = True
                    
                if in_team:
                    # Strip "123: " prefix
                    cleaned = re.sub(r'^\d+:\s', '', l)
                    team_lines.append(cleaned)
                    
                    if 'id="insights-scroll-section"' in l or '<!-- Awards Section -->' in l:
                        team_lines.pop()
                        break
                        
            if len(team_lines) > 20: # Ensure we got a big chunk
                with open('team_section_recovered.html', 'w') as out:
                    out.write('\n'.join(team_lines))
                print("Recovered {} lines!".format(len(team_lines)))
                break
