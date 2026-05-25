import re

html_content = """
      <div class="pathway-content-block" data-visual="visual-growth">
        <div class="reveal-up">
          <h3>Brand Naming & Messaging</h3>
          <p>Our brand naming and messaging process establishes the verbal foundations of your identity. Through thoughtful exploration, we craft names that are distinctive and enduring, paired with messaging that communicates value and meaning - creating a voice that connects across every audience and interaction.</p>
          <div class="strategy-accordion">
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Brand Naming</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Developing names that are distinctive, memorable, and strategically aligned. Through research and creative exploration, we generate options that capture your essence, resonate with audiences, and endure over time, forming the foundation of your brand’s verbal identity.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Key Brand Messaging</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Crafting messaging frameworks that define your brand’s core truths, benefits, and proof points. Clear, compelling, and adaptable, they ensure consistency across every channel - equipping teams to communicate value, inspire audiences, and build meaningful, lasting brand connections.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Brand Voice & Tone</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Shaping brand voice and tone guidelines that bring your personality to life. By defining how your brand speaks in different contexts, we create consistency, flexibility, and resonance - ensuring every word sounds authentic and builds recognition.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Content Strategy</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Our content strategies align storytelling with business goals, defining themes, formats, and channels that bring your brand to life. We guide how content informs, entertains, and inspires - ensuring relevance, clarity, and impact across every stage of the customer journey.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Copywriting</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Delivering copywriting that translates strategy into compelling narratives. From headlines to long-form, our words capture attention, communicate value, and spark connection. Every piece is crafted to embody your voice, strengthen identity, and move audiences to think, feel, and act.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="pathway-content-block" data-visual="visual-expansion">
        <div class="reveal-up">
          <h3>Brand Design</h3>
          <p>Our brand design process transforms strategy into a distinctive visual system that inspires recognition and builds emotional connection. Through purposeful creativity, we craft a cohesive identity that adapts seamlessly across mediums - ensuring every interaction feels consistent, memorable, and true to your brand’s essence.</p>
          <div class="strategy-accordion">
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Brand Identity</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Creating distinctive brand identities that express who you are and why you matter. Through thoughtful and meaningful design choices, we capture essence and personality, building a visual language that inspires recognition, trust, and emotional connection with the audiences who matter most.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Brand Guidelines & Design Systems</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Developing brand guidelines and design systems that ensure clarity, consistency, and creative flexibility. By defining standards for expression, we empower teams to apply the brand with confidence - delivering cohesive, scalable experiences across every channel, platform, and point of interaction.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Art Direction</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Our art direction shapes the visual storytelling that surrounds your brand. From imagery to composition, we establish a creative lens that inspires coherence and distinction - ensuring every campaign, shoot, and asset reflects your essence while standing out in the marketplace.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>CGI & 3D</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Harnessing CGI and 3D design to bring brands to life in dynamic, immersive ways. From product visualisation to experiential storytelling, these tools create impact, depth, and differentiation - helping audiences see and feel your brand beyond traditional static expression.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Motion Design</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Motion design adds energy, rhythm, and emotion to your brand. We craft animated identities, graphics, and storytelling moments that engage audiences and enhance digital experiences - ensuring your brand moves with purpose, creativity, and consistency across platforms and interactions.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="pathway-content-block" data-visual="visual-modernization">
        <div class="reveal-up">
          <h3>Brand & Marketing Application</h3>
          <p>Our brand and marketing application process transforms strategy and design into practical expressions that drive connection and impact. The outcome is a cohesive suite of assets and experiences that ensure your brand is communicated consistently, creatively, and effectively across every touchpoint.</p>
          <div class="strategy-accordion">
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Corporate Presentation Design</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Designing presentations that balance clarity with impact. By uniting storytelling and visual expression, we help teams communicate with confidence - whether persuading stakeholders, inspiring employees, or winning new business - ensuring every presentation becomes a powerful extension of your brand.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Corporate Stationery Suite</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Our stationery suites embed your brand into everyday interactions with professionalism and consistency. From first impressions to lasting touchpoints, we design materials that carry your identity with clarity and distinction, reinforcing credibility in even the smallest details.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Marketing Collateral</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Creating marketing collateral that translates your brand into persuasive tools for engagement. Designed for flexibility and effectiveness, these assets communicate value clearly, build recognition, and support campaigns - ensuring every piece works seamlessly to strengthen connection with your audiences.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Event Marketing</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Designing event marketing campaigns and materials that amplifies your brand presence and creates memorable experiences. From booth design to on-site activations, every detail is crafted to engage audiences, build energy, and leave lasting impressions that connect your brand with moments that matter.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Signage, Environmental & Way-finding</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Creating signage and way-finding systems that bring clarity, coherence, and brand presence to physical spaces. By uniting function with expression, we guide movement and orientation while reinforcing identity - transforming environments into intuitive, meaningful experiences that feel unmistakably yours.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Video & Motion Graphics</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Producing video and motion graphics that animate your brand with energy and emotion. From narrative storytelling to dynamic visual systems, these moving expressions deepen engagement and bring your identity to life across digital platforms and real-world experiences.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="pathway-content-block" data-visual="visual-web-design">
        <div class="reveal-up">
          <h3>Website Design</h3>
          <p>Our website design process blends creativity and usability to create digital experiences that are intuitive, engaging, and distinctly on-brand. This culminates in a seamless online presence - crafted to inspire confidence, communicate value, and connect meaningfully with audiences across every interaction.</p>
          <div class="strategy-accordion">
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>User Experience (UX)</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Designing user experiences that prioritise clarity, simplicity, and flow. By understanding audience needs and behaviours, we shape journeys that feel intuitive and rewarding - ensuring every interaction builds trust, removes friction, and strengthens connection with your brand online.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>User Interface (UI)</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Our user interface design brings your digital brand to life with clarity and distinction. Through thoughtful layout, typography, and visual systems, we create interfaces that are both engaging and functional - delivering beauty and usability in equal measure across every device.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Wireframe & Prototyping</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Utilising wireframing and prototyping to map, test, and refine digital journeys before design is finalised. This process allows us to explore ideas, validate functionality, and ensure the finished website feels seamless, purposeful, and user-centred from the start.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Website Design</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Crafting websites that unite design, content, and technology into cohesive digital experiences. Distinctive yet functional, our designs communicate your brand clearly, adapt seamlessly across devices, and deliver lasting impact - ensuring your online presence is as powerful as your identity.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="pathway-content-block" data-visual="visual-web-dev">
        <div class="reveal-up">
          <h3>Website Development</h3>
          <p>Our website development process transforms design into seamless, high-performing digital platforms. The outcome is a robust online experience built with precision, flexibility, and scalability - that ensures your brand delivers consistent functionality, reliability, and impact across every device, interaction, and audience touchpoint.</p>
          <div class="strategy-accordion">
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Creative Development</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Bringing concepts to life through creative development that bridges design and technology. By exploring innovative solutions and interactions, we ensure every website feels distinctive, engaging, and on-brand - delivering experiences that captivate users and reflect your vision with clarity.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Front-End Development</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Our front-end development translates design into responsive, intuitive interfaces. With a focus on speed, accessibility, and precision, we craft digital experiences that perform flawlessly across devices - ensuring users engage seamlessly while your brand identity shines through every detail.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Back-End Development</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Building reliable, scalable back-end systems that power digital experiences behind the scenes. From data management to complex functionality, our solutions ensure security, performance, and flexibility - providing the foundation for websites that adapt as your business grows and evolves.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>API Integrations</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Implementing API integrations that connect platforms and unlock extended functionality. By seamlessly linking systems, tools, and services, we create websites that are more efficient, powerful, and user-centric - delivering connected digital ecosystems tailored to your business needs.</div>
              </div>
            </div>
            <div class="strategy-acc-item">
              <div class="strategy-acc-header">
                <span>Quality Assurance</span>
                <span class="strategy-acc-icon">+</span>
              </div>
              <div class="strategy-acc-body">
                <div class="strategy-acc-content">Our quality assurance process ensures your website performs flawlessly before launch. Through rigorous testing across devices, browsers, and use cases, we identify and resolve issues early - delivering digital experiences that are seamless, reliable, and ready to perform at every interaction.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
"""

with open('about.html', 'r') as f:
    text = f.read()

# Replace the block from <div class="pathway-content-block" data-visual="visual-growth"> down to the end of visual-modernization
start_str = '<div class="pathway-content-block" data-visual="visual-growth">'
end_str = '<!-- Large Landscape Image Separator -->'
start_idx = text.find(start_str)
end_idx = text.find(end_str)

# We need to preserve the closing div for .pathways-text-content and closing section
if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + html_content + '    </div>\n  </section>\n\n  ' + text[end_idx:]
    with open('about.html', 'w') as f:
        f.write(new_text)
    print("Replaced text content.")

# Now we need to add the two new visual blocks in .pathways-visuals
visuals_insert_point = '<div class="pathway-shape-container" id="visual-modernization">'
visuals_end_idx = text.find('</div>\n    </div>\n\n    <!-- Right Column: Scrolling Text -->')

new_visuals = """
      <div class="pathway-shape-container" id="visual-web-design">
        <div class="geo-pyramid-stack" style="transform: scale(0.8);">
          <div class="geo-hex" style="background: #2a9d8f;"></div>
        </div>
      </div>
      <div class="pathway-shape-container" id="visual-web-dev">
        <div class="geo-pyramid-stack" style="transform: scale(0.8);">
           <div class="geo-hex" style="background: #e76f51;"></div>
        </div>
      </div>
"""

with open('about.html', 'r') as f:
    text = f.read()

idx = text.find('</div>\n    </div>\n\n    <!-- Right Column: Scrolling Text -->')
if idx != -1:
    # insert before the closing div of .pathways-visuals
    new_text = text[:idx+6] + new_visuals + text[idx+6:]
    with open('about.html', 'w') as f:
        f.write(new_text)
    print("Added new visuals.")
