import base64
import os
import subprocess

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
hero_img_path = os.path.join(base_dir, "ELENA_HERO.jpg")
html_out_path = os.path.join(base_dir, "guide_printable.html")
pdf_out_path = os.path.join(base_dir, "The_21_Day_Gentle_Wall_Reset_Guide.pdf")

with open(hero_img_path, "rb") as f:
    hero_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>The 21-Day Gentle Wall Reset Guide - Coach Elena Vance</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    @page {{
      size: A4;
      margin: 14mm 16mm 14mm 16mm;
      @bottom-right {{
        content: counter(page);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 9pt;
        color: #64748b;
      }}
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #1e293b;
      background: #ffffff;
      font-size: 10pt;
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
    }}

    h1, h2, h3, h4 {{
      color: #0f2e22;
      font-weight: 700;
      letter-spacing: -0.02em;
    }}

    .serif {{
      font-family: 'Playfair Display', Georgia, serif;
    }}

    .page {{
      page-break-after: always;
      position: relative;
      height: 100%;
      min-height: 255mm;
      display: flex;
      flex-direction: column;
    }}

    .page:last-child {{
      page-break-after: avoid;
    }}

    /* Cover Page */
    .cover {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      padding: 20mm 10mm 10mm 10mm;
      background: linear-gradient(180deg, #f0f7f3 0%, #ffffff 60%);
      border: 1px solid #d1fae5;
      border-radius: 16px;
    }}

    .cover-tag {{
      display: inline-block;
      background: #0f2e22;
      color: #34d399;
      font-size: 8pt;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 9999px;
      margin-bottom: 12px;
    }}

    .cover-title {{
      font-size: 28pt;
      line-height: 1.15;
      color: #064e3b;
      margin-bottom: 8px;
    }}

    .cover-subtitle {{
      font-size: 13pt;
      color: #374151;
      max-width: 480px;
      margin: 0 auto 20px auto;
      font-weight: 400;
    }}

    .cover-img-wrapper {{
      width: 170px;
      height: 170px;
      border-radius: 50%;
      overflow: hidden;
      border: 4px solid #064e3b;
      box-shadow: 0 10px 25px -5px rgba(6, 78, 59, 0.25);
      margin: 0 auto 20px auto;
    }}

    .cover-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .cover-author {{
      font-size: 11pt;
      font-weight: 700;
      color: #064e3b;
    }}

    .cover-author-title {{
      font-size: 9pt;
      color: #64748b;
      margin-bottom: 25px;
    }}

    .cover-pills {{
      display: flex;
      gap: 12px;
      justify-content: center;
      margin-bottom: 20px;
    }}

    .cover-pill {{
      background: #ffffff;
      border: 1px solid #a7f3d0;
      padding: 6px 14px;
      border-radius: 10px;
      font-size: 8pt;
      font-weight: 600;
      color: #065f46;
    }}

    /* Standard Page Header */
    .page-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 8px;
      margin-bottom: 16px;
    }}

    .header-logo {{
      font-size: 9pt;
      font-weight: 700;
      color: #064e3b;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}

    .header-week {{
      font-size: 8.5pt;
      font-weight: 600;
      color: #059669;
      background: #ecfdf5;
      padding: 3px 10px;
      border-radius: 6px;
    }}

    /* Cards & Blocks */
    .card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }}

    .card-highlight {{
      background: #f0fdf4;
      border: 1.5px solid #bbf7d0;
    }}

    .card-warning {{
      background: #fffbeb;
      border: 1.5px solid #fde68a;
    }}

    .card-title {{
      font-size: 11pt;
      font-weight: 700;
      color: #064e3b;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .exercise-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-left: 4px solid #059669;
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 12px;
    }}

    .exercise-day {{
      font-size: 8pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #059669;
    }}

    .exercise-name {{
      font-size: 11pt;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 6px;
    }}

    .exercise-meta {{
      display: flex;
      gap: 12px;
      font-size: 8.5pt;
      font-weight: 600;
      color: #475569;
      margin-bottom: 8px;
    }}

    .exercise-meta span {{
      background: #f1f5f9;
      padding: 2px 8px;
      border-radius: 4px;
    }}

    .step-list {{
      padding-left: 16px;
      font-size: 9.5pt;
      color: #334155;
    }}

    .step-list li {{
      margin-bottom: 4px;
    }}

    .quote-box {{
      font-style: italic;
      color: #064e3b;
      background: #ecfdf5;
      border-left: 3px solid #059669;
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      margin: 12px 0;
      font-size: 9.5pt;
    }}

    /* Table Tracker */
    .tracker-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
      font-size: 8.5pt;
    }}

    .tracker-table th {{
      background: #064e3b;
      color: #ffffff;
      text-align: left;
      padding: 8px 10px;
      font-weight: 600;
    }}

    .tracker-table td {{
      border-bottom: 1px solid #e2e8f0;
      padding: 7px 10px;
      color: #334155;
    }}

    .tracker-table tr:nth-child(even) {{
      background: #f8fafc;
    }}

    .checkbox-box {{
      display: inline-block;
      width: 13px;
      height: 13px;
      border: 1.5px solid #94a3b8;
      border-radius: 3px;
    }}

    .footer-note {{
      margin-top: auto;
      text-align: center;
      font-size: 8pt;
      color: #94a3b8;
      border-top: 1px solid #f1f5f9;
      padding-top: 8px;
    }}
  </style>
</head>
<body>

  <!-- PAGE 1: COVER -->
  <div class="page cover">
    <div>
      <div class="cover-tag">Official Somatic Protocol</div>
      <h1 class="cover-title serif">The 21-Day Gentle<br>Wall Reset Guide</h1>
      <p class="cover-subtitle">A Zero-Floor Somatic Restoration Protocol for Women 45+ to Release Lower Back Stiffness, Lubricate Stiff Hips & Free Your Knees.</p>
    </div>

    <div>
      <div class="cover-img-wrapper">
        <img class="cover-img" src="data:image/jpeg;base64,{hero_b64}" alt="Coach Elena Vance">
      </div>
      <div class="cover-author">Coach Elena Vance</div>
      <div class="cover-author-title">51-Year-Old Somatic Mobility & Joint Decompression Specialist<br>Instagram: @coach.elena.vance</div>

      <div class="cover-pills">
        <div class="cover-pill">0% Floor Kneeling</div>
        <div class="cover-pill">5 Minutes A Day</div>
        <div class="cover-pill">Zero Equipment Needed</div>
      </div>
    </div>

    <div style="font-size: 8.5pt; color: #64748b;">
      Copyright &copy; 2026 Coach Elena Vance. All Rights Reserved.<br>Personal Use License for Digital Buyers.
    </div>
  </div>

  <!-- PAGE 2: WELCOME & PHILOSOPHY -->
  <div class="page">
    <div class="page-header">
      <span class="header-logo">The 21-Day Gentle Wall Reset</span>
      <span class="header-week">Introduction &amp; Welcome</span>
    </div>

    <h2 class="serif" style="font-size: 18pt; margin-bottom: 10px; color: #064e3b;">Welcome from Coach Elena</h2>

    <div class="quote-box">
      "If you wake up feeling like your lower back is locked in concrete, your hips pop when getting up from a chair, or your knees ache going down stairs—I need you to hear this: <strong>your body is not broken.</strong> It is simply trapped in a protective nervous system lock."
    </div>

    <p style="margin-bottom: 12px; color: #334155;">
      Traditional fitness insists that women over 40 must stretch aggressively on hard floors, hold punishing planks, or do deep yoga squats. But when you force an already inflamed joint past its comfort zone on a hard hardwood floor, your autonomic nervous system does the exact opposite of relaxing: it triggers a <em>muscular guarding reflex</em>, locking your lumbar spine and psoas even tighter.
    </p>

    <div class="card card-highlight">
      <div class="card-title">Why The Wall Changes Everything</div>
      <p style="font-size: 9.5pt; color: #166534;">
        By standing and utilizing the solid vertical support of an ordinary wall, you achieve three clinical advantages:
      </p>
      <ul class="step-list" style="margin-top: 6px;">
        <li><strong>Zero Patella Pressure:</strong> You never have to kneel on knees with thinning meniscus or sensitive joints.</li>
        <li><strong>Instant Lumbar Decompression:</strong> The wall offloads gravity from the L4-L5 vertebrae, allowing discs to rehydrate naturally.</li>
        <li><strong>Nervous System Safety:</strong> Total balance stability signals the brain that you are safe, dissolving involuntary muscle tension.</li>
      </ul>
    </div>

    <div class="card card-warning">
      <div class="card-title">The 3 Golden Rules of This Reset</div>
      <ol class="step-list" style="padding-left: 18px;">
        <li><strong>Never Force Past a Pinch:</strong> Somatic release is gentle communication with your fascia, not an endurance test. Stay strictly within pain-free zones.</li>
        <li><strong>Exhale Longer Than You Inhale:</strong> Inhale for 4 seconds through your nose, exhale for 6 seconds through parted lips. This activates your vagus nerve.</li>
        <li><strong>Consistency Beats Intensity:</strong> Doing 5 gentle minutes every single morning creates lasting neuro-muscular transformation.</li>
      </ol>
    </div>

    <div class="footer-note">
      Coach Elena Vance &bull; The 21-Day Gentle Wall Reset &bull; Page 2
    </div>
  </div>

  <!-- PAGE 3: WEEK 1 (DAYS 1 TO 7) -->
  <div class="page">
    <div class="page-header">
      <span class="header-logo">The 21-Day Gentle Wall Reset</span>
      <span class="header-week">Week 1: Days 1 to 7</span>
    </div>

    <h2 class="serif" style="font-size: 16pt; margin-bottom: 6px; color: #064e3b;">Week 1: Spinal &amp; Lumbar Decompression</h2>
    <p style="font-size: 9pt; color: #475569; margin-bottom: 14px;">
      <strong>Core Focus:</strong> Unlocking the L4-L5 spinal junction, resetting morning stiffness, and creating space between compressed vertebrae.
    </p>

    <!-- Ex 1 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 1 &ndash; 3 &bull; Morning Routine</div>
      <div class="exercise-name">The Wall Palms Press</div>
      <div class="exercise-meta">
        <span>3 Sets &times; 30 Seconds</span>
        <span>Target: Lower Back &amp; Shoulders</span>
      </div>
      <ol class="step-list">
        <li>Stand facing the wall, roughly an arm's length away. Feet hip-width apart.</li>
        <li>Place both palms flat on the wall at mid-chest height, fingers spread wide.</li>
        <li>Take a half-step back, hinge slightly at the hips, and let your head rest comfortably between your arms.</li>
        <li>Inhale deeply into your belly for 4 seconds; exhale for 6 seconds as you let your chest soften toward the floor.</li>
        <li><strong>What you should feel:</strong> A gentle lengthening sensation down your spine and mid-back without pinching.</li>
      </ol>
    </div>

    <!-- Ex 2 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 4 &ndash; 5 &bull; Morning Routine</div>
      <div class="exercise-name">Standing Spinal Lengthening</div>
      <div class="exercise-meta">
        <span>3 Sets &times; 45 Seconds</span>
        <span>Target: L4-L5 Decompression &amp; Hamstrings</span>
      </div>
      <ol class="step-list">
        <li>With palms anchored on the wall at shoulder height, keep a soft micro-bend in both knees.</li>
        <li>Slowly shift your hips backward, creating an "L" shape with your torso and legs.</li>
        <li>Do not lock your knees. Feel gravity tractioning your lower back away from your ribs.</li>
        <li>Hold for 5 deep, slow diaphragmatic breaths per set.</li>
      </ol>
    </div>

    <!-- Ex 3 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 6 &ndash; 7 &bull; Morning Routine</div>
      <div class="exercise-name">The Morning Wall Breath Sync</div>
      <div class="exercise-meta">
        <span>2 Minutes Continuous</span>
        <span>Target: Autonomic Nervous System Reset</span>
      </div>
      <ol class="step-list">
        <li>Rest your forehead gently against the back of your hands on the wall.</li>
        <li>Place your feet securely. Close your eyes.</li>
        <li>Breathe in slowly through your nose for 4 counts, expanding your ribcage 360 degrees.</li>
        <li>Exhale slowly with an audible "sigh" for 6 counts. Repeat for 10 complete breath cycles.</li>
      </ol>
    </div>

    <div class="footer-note">
      Coach Elena Vance &bull; The 21-Day Gentle Wall Reset &bull; Page 3
    </div>
  </div>

  <!-- PAGE 4: WEEK 2 (DAYS 8 TO 14) -->
  <div class="page">
    <div class="page-header">
      <span class="header-logo">The 21-Day Gentle Wall Reset</span>
      <span class="header-week">Week 2: Days 8 to 14</span>
    </div>

    <h2 class="serif" style="font-size: 16pt; margin-bottom: 6px; color: #064e3b;">Week 2: Hip Lubrication &amp; Pelvic Alignment</h2>
    <p style="font-size: 9pt; color: #475569; margin-bottom: 14px;">
      <strong>Core Focus:</strong> Rehydrating the synovial fluid in your hip sockets, freeing the tight psoas muscle, and stabilizing the sacroiliac (SI) joints.
    </p>

    <!-- Ex 4 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 8 &ndash; 10 &bull; Daily Routine</div>
      <div class="exercise-name">Supported Standing Hip Circles</div>
      <div class="exercise-meta">
        <span>30 Seconds per side &bull; 2 Sets</span>
        <span>Target: Acetabular Joint Lubrication</span>
      </div>
      <ol class="step-list">
        <li>Stand sideways to the wall. Rest your inside hand flat on the wall for 100% stable balance.</li>
        <li>Lift your outside foot just 2 inches off the ground.</li>
        <li>Draw slow, smooth micro-circles in the air with your knee (5 clockwise, 5 counter-clockwise).</li>
        <li>Keep the movement small, controlled, and buttery-smooth. Turn and repeat on the other side.</li>
      </ol>
    </div>

    <!-- Ex 5 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 11 &ndash; 12 &bull; Daily Routine</div>
      <div class="exercise-name">The Wall Pelvic Tilt</div>
      <div class="exercise-meta">
        <span>10 Slow Repetitions &bull; 2 Sets</span>
        <span>Target: Pelvic Alignment &amp; Sacrum Reset</span>
      </div>
      <ol class="step-list">
        <li>Lean your upper back and glutes flat against the wall, heels placed 4 inches away.</li>
        <li>Notice the natural arch in your lower back.</li>
        <li>Gently engage your lower abdomen and flatten your lower back flush against the wall.</li>
        <li>Hold flat for 3 seconds, then slowly release back to neutral. Repeat 10 deliberate times.</li>
      </ol>
    </div>

    <!-- Ex 6 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 13 &ndash; 14 &bull; Daily Routine</div>
      <div class="exercise-name">The Standing Psoas Release (Zero Floor Work)</div>
      <div class="exercise-meta">
        <span>45 Seconds per side</span>
        <span>Target: Deep Hip Flexors &amp; Sciatic Pathway</span>
      </div>
      <ol class="step-list">
        <li>Both hands on the wall at shoulder height. Step your right leg back in a small stagger.</li>
        <li>Keep both heels flat on the floor. Gently tuck your tailbone under (posterior pelvic tilt).</li>
        <li>Shift your weight slightly forward into your front knee until you feel a long, soothing release across the front of your right hip.</li>
        <li>Breathe smoothly for 45 seconds, then switch legs.</li>
      </ol>
    </div>

    <div class="footer-note">
      Coach Elena Vance &bull; The 21-Day Gentle Wall Reset &bull; Page 4
    </div>
  </div>

  <!-- PAGE 5: WEEK 3 (DAYS 15 TO 21) -->
  <div class="page">
    <div class="page-header">
      <span class="header-logo">The 21-Day Gentle Wall Reset</span>
      <span class="header-week">Week 3: Days 15 to 21</span>
    </div>

    <h2 class="serif" style="font-size: 16pt; margin-bottom: 6px; color: #064e3b;">Week 3: Full-Chain Integration &amp; Habit</h2>
    <p style="font-size: 9pt; color: #475569; margin-bottom: 14px;">
      <strong>Core Focus:</strong> Connecting upper thoracic posture with pelvic mobility, freeing knee glide, and cementing your lifelong 5-minute morning routine.
    </p>

    <!-- Ex 7 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 15 &ndash; 17 &bull; Daily Routine</div>
      <div class="exercise-name">The Supported Wall Angels</div>
      <div class="exercise-meta">
        <span>8 Slow Repetitions &bull; 2 Sets</span>
        <span>Target: Postural Re-alignment &amp; Upper Spine</span>
      </div>
      <ol class="step-list">
        <li>Stand with your head, upper back, and buttocks lightly contacting the wall.</li>
        <li>Bring arms up in a "cactus" or "W" shape, elbows and back of wrists against the wall.</li>
        <li>Slowly glide your arms upwards 3 to 6 inches, keeping contact with the wall.</li>
        <li>Only go as high as comfortable without overarching your lower back. Lower smoothly.</li>
      </ol>
    </div>

    <!-- Ex 8 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 18 &ndash; 19 &bull; Daily Routine</div>
      <div class="exercise-name">The Full-Chain Wall Reset</div>
      <div class="exercise-meta">
        <span>3 Minutes Flow</span>
        <span>Target: Whole Body Mobility</span>
      </div>
      <ol class="step-list">
        <li>Flow seamlessly: 60s Wall Palms Press &rarr; 60s Supported Hip Circles &rarr; 60s Pelvic Tilts.</li>
        <li>Allow each breath to guide the transition. You will feel warmth spreading through joints.</li>
      </ol>
    </div>

    <!-- Ex 9 -->
    <div class="exercise-box">
      <div class="exercise-day">Days 20 &ndash; 21 &bull; Forever Practice</div>
      <div class="exercise-name">Your Lifelong 5-Minute Morning Reset</div>
      <div class="exercise-meta">
        <span>5 Minutes Daily &bull; Lifelong Habit</span>
        <span>Target: Daily Anti-Stiffness Protection</span>
      </div>
      <ol class="step-list">
        <li><strong>Minute 1:</strong> Wall Palms Press (Spinal Decompression).</li>
        <li><strong>Minute 2:</strong> Hip Circles (30s right, 30s left).</li>
        <li><strong>Minute 3:</strong> Standing Psoas Release (30s right, 30s left).</li>
        <li><strong>Minute 4:</strong> Wall Angels (5 slow reps).</li>
        <li><strong>Minute 5:</strong> Wall Breath Sync (Reset nervous system before your morning coffee).</li>
      </ol>
    </div>

    <div class="footer-note">
      Coach Elena Vance &bull; The 21-Day Gentle Wall Reset &bull; Page 5
    </div>
  </div>

  <!-- PAGE 6: BONUS PROTOCOL & 21-DAY TRACKER -->
  <div class="page">
    <div class="page-header">
      <span class="header-logo">The 21-Day Gentle Wall Reset</span>
      <span class="header-week">Bonuses &amp; Progress Tracker</span>
    </div>

    <h2 class="serif" style="font-size: 16pt; margin-bottom: 6px; color: #064e3b;">Exclusive Bonus: The 30-Second Travel Fix</h2>
    <div class="card card-highlight" style="margin-bottom: 14px;">
      <p style="font-size: 9.5pt; color: #166534; margin-bottom: 6px;">
        <strong>When to use:</strong> Whenever you step out of a car after a long drive, get up from a 2-hour movie, or finish desk work.
      </p>
      <p style="font-size: 9.5pt; color: #334155;">
        Walk to any wall or doorway. Place hands at shoulder height. Step back into the <strong>Standing Spinal Lengthening</strong> pose. Take 3 slow, deep belly exhales. Your pelvis will instantly un-tuck and synovial fluid will rush back to lubricate your hip joints.
      </p>
    </div>

    <h3 style="font-size: 13pt; margin-bottom: 6px; color: #064e3b;">Your 21-Day Commitment Tracker</h3>
    <p style="font-size: 8.5pt; color: #64748b; margin-bottom: 8px;">
      Check off each day as you complete your 5-minute morning routine:
    </p>

    <table class="tracker-table">
      <thead>
        <tr>
          <th>Day</th>
          <th>Routine</th>
          <th>Done</th>
          <th>How Did Your Body Feel?</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Day 1</td><td>Wall Palms Press (3x30s)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Morning back stiffness rating: ___/10</td></tr>
        <tr><td>Day 2</td><td>Wall Palms Press (3x30s)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Notice breathing depth</td></tr>
        <tr><td>Day 3</td><td>Wall Palms Press (3x30s)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Shoulders feeling lighter</td></tr>
        <tr><td>Day 4</td><td>Spinal Lengthening (3x45s)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Lower spine decompression</td></tr>
        <tr><td>Day 5</td><td>Spinal Lengthening (3x45s)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Notice hamstring softness</td></tr>
        <tr><td>Day 6</td><td>Wall Breath Sync (2 min)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Nervous system calm</td></tr>
        <tr><td>Day 7</td><td>Week 1 Review &amp; Rest</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>End of Week 1 milestone!</td></tr>
        <tr><td>Day 8</td><td>Hip Circles (30s/side)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Hip clicking reducing</td></tr>
        <tr><td>Day 9</td><td>Hip Circles (30s/side)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Smoother range of motion</td></tr>
        <tr><td>Day 10</td><td>Hip Circles (30s/side)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Standing easier from chairs</td></tr>
        <tr><td>Day 11</td><td>Wall Pelvic Tilt (10 reps)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Core and pelvis connection</td></tr>
        <tr><td>Day 12</td><td>Wall Pelvic Tilt (10 reps)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Sacrum tension releasing</td></tr>
        <tr><td>Day 13</td><td>Standing Psoas (45s/side)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Deep front hip opening</td></tr>
        <tr><td>Day 14</td><td>Week 2 Review &amp; Rest</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>End of Week 2 milestone!</td></tr>
        <tr><td>Day 15</td><td>Wall Angels (8 reps)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Upright, taller posture</td></tr>
        <tr><td>Day 16</td><td>Wall Angels (8 reps)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Neck &amp; upper back relief</td></tr>
        <tr><td>Day 17</td><td>Wall Angels (8 reps)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Fluid arm extension</td></tr>
        <tr><td>Day 18</td><td>Full-Chain Flow (3 min)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Total body lightness</td></tr>
        <tr><td>Day 19</td><td>Full-Chain Flow (3 min)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Energy feels renewed</td></tr>
        <tr><td>Day 20</td><td>Lifelong Morning Reset (5 min)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td>Automatic habit formed!</td></tr>
        <tr><td>Day 21</td><td>Lifelong Morning Reset (5 min)</td><td style="text-align:center;"><div class="checkbox-box"></div></td><td><strong>Full Reset Complete!</strong></td></tr>
      </tbody>
    </table>

    <div style="margin-top: 14px; text-align: center; background: #ecfdf5; border: 1px dashed #059669; border-radius: 8px; padding: 8px;">
      <p style="font-size: 8.5pt; color: #064e3b; font-weight: 600;">
        Need advice or want to share your 21-day results? DM me on Instagram: <strong>@coach.elena.vance</strong>
      </p>
    </div>

    <div class="footer-note">
      Coach Elena Vance &bull; The 21-Day Gentle Wall Reset &bull; Page 6
    </div>
  </div>

</body>
</html>
"""

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML saved to {html_out_path}")

# Run msedge to generate PDF
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={pdf_out_path}",
    html_out_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge returncode:", res.returncode)
if os.path.exists(pdf_out_path):
    print(f"SUCCESS: PDF created at {pdf_out_path} (Size: {os.path.getsize(pdf_out_path)} bytes)")
else:
    print("FAILED: PDF not created")
    print("Stderr:", res.stderr)
