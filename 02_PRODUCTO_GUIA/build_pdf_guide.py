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


def get_posture_svg(pose_type: str, target_zone: str) -> str:
    """Returns a custom minimalist architectural & somatic SVG diagram for each daily exercise."""
    wall_left = """
      <!-- Architectural Wall Structure -->
      <rect x="22" y="18" width="10" height="164" rx="2" fill="#E5DEC9" stroke="#46594B" stroke-width="1.4"/>
      <line x1="22" y1="35" x2="32" y2="25" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="55" x2="32" y2="45" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="75" x2="32" y2="65" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="95" x2="32" y2="85" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="115" x2="32" y2="105" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="135" x2="32" y2="125" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="155" x2="32" y2="145" stroke="#8C7A6B" stroke-width="1"/>
      <line x1="22" y1="175" x2="32" y2="165" stroke="#8C7A6B" stroke-width="1"/>
      <!-- Floor Line -->
      <line x1="16" y1="182" x2="204" y2="182" stroke="#46594B" stroke-width="1.5" stroke-linecap="round"/>
    """

    diagrams = {
        "palms_press": f"""
          {wall_left}
          <!-- Distance Marker -->
          <line x1="34" y1="168" x2="92" y2="168" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="3 2"/>
          <text x="63" y="163" font-family="JetBrains Mono, monospace" font-size="6.5" fill="#B86F4C" text-anchor="middle">ARM'S LENGTH</text>
          <!-- Somatic Figure Facing Wall -->
          <circle cx="92" cy="54" r="10" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <!-- Arms Pressing Wall -->
          <path d="M88 68 L34 72" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <circle cx="34" cy="72" r="3.5" fill="#B86F4C"/>
          <!-- Torso & Gentle Hinge -->
          <path d="M92 64 Q98 92 102 116" fill="none" stroke="#18221B" stroke-width="2.4" stroke-linecap="round"/>
          <!-- Target Decompression Glow (L4-L5 & Thoracic) -->
          <circle cx="99" cy="102" r="9" fill="#B86F4C" fill-opacity="0.18" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <circle cx="99" cy="102" r="3.5" fill="#B86F4C"/>
          <!-- Legs Standing -->
          <path d="M102 116 L96 150 L96 181" fill="none" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <!-- Decompression Vector Arrows -->
          <path d="M114 82 Q122 98 118 114" fill="none" stroke="#46594B" stroke-width="1.4" stroke-dasharray="2 2"/>
          <polygon points="118,116 115,110 121,111" fill="#46594B"/>
          <text x="148" y="42" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#46594B">AXIAL OFF-LOAD</text>
          <text x="148" y="53" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#647A68">Palms at chest level</text>
        """,
        "l_traction": f"""
          {wall_left}
          <!-- L-Shape Hinge Figure -->
          <circle cx="78" cy="78" r="9" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <!-- Extended Arms to Wall -->
          <line x1="34" y1="84" x2="128" y2="84" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <circle cx="34" cy="84" r="3.5" fill="#B86F4C"/>
          <!-- Lumbar Decompression Zone -->
          <circle cx="126" cy="84" r="11" fill="#B86F4C" fill-opacity="0.18" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <circle cx="126" cy="84" r="4" fill="#B86F4C"/>
          <!-- Soft Micro-Bent Knees -->
          <path d="M128 84 L122 134 L128 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Traction Arrow Backward -->
          <line x1="138" y1="84" x2="168" y2="84" stroke="#B86F4C" stroke-width="1.5"/>
          <polygon points="172,84 165,80 165,88" fill="#B86F4C"/>
          <text x="155" y="74" font-family="JetBrains Mono, monospace" font-size="6.8" font-weight="700" fill="#B86F4C" text-anchor="middle">L4-L5 TRACTION</text>
          <text x="145" y="138" font-family="JetBrains Mono, monospace" font-size="6.5" fill="#46594B">SOFT KNEES</text>
        """,
        "spinal_wave": f"""
          {wall_left}
          <!-- Standing Wave Figure -->
          <circle cx="88" cy="52" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <path d="M82 68 L34 78" stroke="#18221B" stroke-width="2" stroke-linecap="round"/>
          <!-- Dual Curve Spine (Cat/Cow Wave) -->
          <path d="M88 62 Q76 88 94 116" fill="none" stroke="#46594B" stroke-width="2.2" stroke-dasharray="3 2"/>
          <path d="M88 62 Q104 88 94 116" fill="none" stroke="#18221B" stroke-width="2.4" stroke-linecap="round"/>
          <!-- Target Nodes Along Spine -->
          <circle cx="95" cy="76" r="3" fill="#B86F4C"/>
          <circle cx="98" cy="92" r="3.5" fill="#B86F4C"/>
          <circle cx="95" cy="108" r="3" fill="#B86F4C"/>
          <path d="M94 116 L90 150 L92 181" fill="none" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <text x="148" y="86" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#B86F4C">SEGMENTAL WAVE</text>
          <text x="148" y="97" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#46594B">Inhale arch · Exhale round</text>
        """,
        "lateral_arc": f"""
          {wall_left}
          <!-- Sideways Ribcage Arc -->
          <circle cx="86" cy="48" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <path d="M78 60 L34 62" stroke="#18221B" stroke-width="2" stroke-linecap="round"/>
          <!-- Overhead Reach Arc -->
          <path d="M86 58 Q72 26 42 34" fill="none" stroke="#B86F4C" stroke-width="1.8" stroke-dasharray="3 2"/>
          <!-- Curved Lateral Torso -->
          <path d="M86 58 Q112 88 96 118" fill="none" stroke="#18221B" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="104" cy="90" r="10" fill="#B86F4C" fill-opacity="0.18" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <circle cx="104" cy="90" r="3.5" fill="#B86F4C"/>
          <path d="M96 118 L92 181" fill="none" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <text x="148" y="88" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#B86F4C">QL &amp; RIBCAGE ARC</text>
          <text x="148" y="99" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#46594B">Side-body decompression</text>
        """,
        "hip_circles": f"""
          {wall_left}
          <!-- Upright Side Support Figure -->
          <circle cx="88" cy="46" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <line x1="88" y1="56" x2="88" y2="112" stroke="#18221B" stroke-width="2.4" stroke-linecap="round"/>
          <line x1="88" y1="74" x2="34" y2="74" stroke="#18221B" stroke-width="2.1" stroke-linecap="round"/>
          <circle cx="34" cy="74" r="3.5" fill="#46594B"/>
          <!-- Standing Support Leg -->
          <line x1="84" y1="112" x2="84" y2="181" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Lifted Knee & Orbital Circle -->
          <path d="M90 112 L114 132 L110 162" fill="none" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <circle cx="90" cy="112" r="9" fill="#B86F4C" fill-opacity="0.2" stroke="#B86F4C" stroke-width="1.2"/>
          <circle cx="90" cy="112" r="3.5" fill="#B86F4C"/>
          <ellipse cx="116" cy="132" rx="16" ry="11" fill="none" stroke="#B86F4C" stroke-width="1.4" stroke-dasharray="3 2"/>
          <text x="152" y="108" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#B86F4C">SYNOVIAL ORBIT</text>
          <text x="152" y="119" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#46594B">5 slow circles each way</text>
        """,
        "pelvic_tilt": f"""
          {wall_left}
          <!-- Back Against Wall Figure -->
          <circle cx="48" cy="46" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <!-- Upper Back & Sacrum Flush to Wall -->
          <path d="M36 58 Q42 84 35 112" fill="none" stroke="#18221B" stroke-width="2.5" stroke-linecap="round"/>
          <!-- Lumbar imprint arrow -->
          <line x1="60" y1="92" x2="38" y2="92" stroke="#B86F4C" stroke-width="1.8"/>
          <polygon points="35,92 41,88 41,96" fill="#B86F4C"/>
          <circle cx="38" cy="106" r="9" fill="#B86F4C" fill-opacity="0.2" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <!-- Legs with 4-inch heel offset -->
          <path d="M36 112 L52 146 L56 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Pelvic Clock Diagram on Right -->
          <circle cx="145" cy="96" r="24" fill="#FAF6F0" stroke="#46594B" stroke-width="1.3"/>
          <path d="M145 78 A18 18 0 0 1 145 114" fill="none" stroke="#B86F4C" stroke-width="1.6" stroke-dasharray="2 2"/>
          <text x="145" y="68" font-family="JetBrains Mono, monospace" font-size="6.5" fill="#46594B" text-anchor="middle">12 O'CLOCK TUCK</text>
          <text x="145" y="130" font-family="JetBrains Mono, monospace" font-size="6.5" fill="#647A68" text-anchor="middle">6 O'CLOCK RELEASE</text>
        """,
        "psoas_release": f"""
          {wall_left}
          <!-- Standing Staggered Stance Facing Wall -->
          <circle cx="82" cy="46" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <line x1="78" y1="66" x2="34" y2="68" stroke="#18221B" stroke-width="2.1" stroke-linecap="round"/>
          <line x1="82" y1="56" x2="84" y2="110" stroke="#18221B" stroke-width="2.4" stroke-linecap="round"/>
          <!-- Front Leg -->
          <path d="M84 110 L70 144 L70 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Back Leg (Psoas Lengthening) -->
          <path d="M84 110 L112 146 L128 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Glowing Psoas Line -->
          <path d="M83 94 Q88 112 100 130" fill="none" stroke="#B86F4C" stroke-width="3" stroke-linecap="round"/>
          <circle cx="88" cy="112" r="9" fill="#B86F4C" fill-opacity="0.18" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <text x="148" y="96" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#B86F4C">ZERO-KNEEL PSOAS</text>
          <text x="148" y="107" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#46594B">Tailbone softly tucked</text>
        """,
        "knee_glide": f"""
          {wall_left}
          <!-- Wall-Supported Knee & Ankle Decompression -->
          <circle cx="80" cy="48" r="9" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <line x1="76" y1="68" x2="34" y2="68" stroke="#18221B" stroke-width="2" stroke-linecap="round"/>
          <line x1="80" y1="58" x2="84" y2="112" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <path d="M84 112 L74 146 L82 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Target Glow on Knee & Ankle -->
          <circle cx="74" cy="146" r="10" fill="#B86F4C" fill-opacity="0.2" stroke="#B86F4C" stroke-width="1.3" stroke-dasharray="2 2"/>
          <circle cx="74" cy="146" r="3.5" fill="#B86F4C"/>
          <circle cx="82" cy="177" r="6" fill="#46594B" fill-opacity="0.2" stroke="#46594B" stroke-width="1.2"/>
          <text x="145" y="138" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#B86F4C">PATELLA OFFLOAD</text>
          <text x="145" y="149" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#46594B">70% weight on wall hands</text>
        """,
        "wall_angels": f"""
          {wall_left}
          <!-- Back Against Wall + Cactus Arms -->
          <circle cx="44" cy="46" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <line x1="36" y1="56" x2="36" y2="114" stroke="#18221B" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M36 114 L48 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Front View Inset Diagram of Cactus Arms -->
          <circle cx="138" cy="60" r="9" fill="#FAF6F0" stroke="#18221B" stroke-width="1.7"/>
          <line x1="138" y1="70" x2="138" y2="124" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <!-- W / Cactus Arms -->
          <path d="M108 58 L116 84 L138 84 L160 84 L168 58" fill="none" stroke="#18221B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
          <!-- Upward Glide Arrows -->
          <line x1="108" y1="52" x2="108" y2="36" stroke="#B86F4C" stroke-width="1.5"/>
          <polygon points="108,33 105,39 111,39" fill="#B86F4C"/>
          <line x1="168" y1="52" x2="168" y2="36" stroke="#B86F4C" stroke-width="1.5"/>
          <polygon points="168,33 165,39 171,39" fill="#B86F4C"/>
          <circle cx="138" cy="84" r="9" fill="#B86F4C" fill-opacity="0.18" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <text x="138" y="146" font-family="JetBrains Mono, monospace" font-size="6.8" font-weight="600" fill="#46594B" text-anchor="middle">SCAPULAR GLIDE</text>
        """,
        "vagal_flow": f"""
          {wall_left}
          <!-- Restorative Forehead on Hands at Wall -->
          <circle cx="56" cy="58" r="9.5" fill="#FAF6F0" stroke="#18221B" stroke-width="1.8"/>
          <path d="M52 64 L34 58" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <path d="M58 68 Q64 94 64 118 L62 181" fill="none" stroke="#18221B" stroke-width="2.3" stroke-linecap="round"/>
          <!-- Concentric Vagal Calm Waves -->
          <circle cx="62" cy="82" r="12" fill="none" stroke="#B86F4C" stroke-width="1.2" stroke-dasharray="2 2"/>
          <circle cx="62" cy="82" r="22" fill="none" stroke="#46594B" stroke-width="1" stroke-dasharray="3 3"/>
          <circle cx="62" cy="82" r="32" fill="none" stroke="#647A68" stroke-width="0.8" stroke-dasharray="4 4"/>
          <text x="145" y="78" font-family="JetBrains Mono, monospace" font-size="7" font-weight="600" fill="#46594B">VAGUS NERVE RESET</text>
          <text x="145" y="90" font-family="Plus Jakarta Sans, sans-serif" font-size="6.5" fill="#B86F4C">4s Inhale · 6s Exhale</text>
        """
    }

    inner = diagrams.get(pose_type, diagrams["palms_press"])
    return f"""
    <svg viewBox="0 0 220 195" class="posture-svg" xmlns="http://www.w3.org/2000/svg">
      <rect x="2" y="2" width="216" height="191" rx="10" fill="#FAF6F0" stroke="#D9CEBE" stroke-width="1"/>
      {inner}
      <rect x="118" y="158" width="90" height="20" rx="4" fill="#F2ECE1" stroke="#D9CEBE" stroke-width="0.8"/>
      <text x="163" y="171" font-family="JetBrains Mono, monospace" font-size="6.2" font-weight="600" fill="#18221B" text-anchor="middle">{target_zone[:20].upper()}</text>
    </svg>
    """


# Complete 21-Day Curriculum (1 Dedicated Page Per Day)
DAYS_DATA = [
    # ==================== WEEK 1: SPINAL & LUMBAR DECOMPRESSION (DAYS 01 - 07) ====================
    {
        "day": 1,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "The Wall Palms Press",
        "subtitle": "Axial Spine Decompression & Morning Guarding Release",
        "duration": "5 Minutes",
        "sets": "3 Sets × 45 Sec",
        "target": "L4–L5 Lumbar & Chest",
        "pose": "palms_press",
        "somatic_why": "Overnight, fluid settles and your paraspinal muscles tighten into a protective morning shell. Pressing your palms gently into a solid vertical wall transfers upper-body weight away from your compressed L4–L5 lumbar discs while signaling immediate postural safety to your brainstem.",
        "setup": "Stand facing a clear wall, approximately one arm's length away. Place your feet hip-width apart with your weight balanced evenly across your heels and mid-foot.",
        "movement": [
            "Place both palms flat against the wall at chest height, fingers spread softly like roots.",
            "Keep a micro-softness behind both knees—never lock your leg joints.",
            "Take a half-step back and allow your chest to melt gently downward between your upper arms while your hands stay anchored.",
            "Feel a long, soothing traction from your tailbone all the way up to the base of your neck."
        ],
        "breath": "Inhale quietly through your nose for 4 seconds, expanding your side ribs. Exhale through softly parted lips for 6 seconds, letting your breastbone sink 1 centimeter closer to the floor.",
        "feel_good": "A warm, gentle lengthening across your mid-back, underarms, and lower lumbar spine.",
        "avoid": "Forcing your head down aggressively or arching your lower back to push deeper.",
        "mod_easy": "Place your hands slightly higher (above shoulder level) and stand closer to the wall for a super-mild release.",
        "mod_deep": "Slide your palms 3 inches lower toward ribcage height and shift your sit-bones softly backward.",
        "elena_note": "Day 1 is not about stretching hard—it is about introducing your nervous system to the feeling of being supported. Let the wall hold you."
    },
    {
        "day": 2,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "The Scapular Wall Melt",
        "subtitle": "Upper Thoracic Unwinding & Shoulder-Blade Glide",
        "duration": "5 Minutes",
        "sets": "3 Sets × 40 Sec",
        "target": "Thoracic Spine & Traps",
        "pose": "palms_press",
        "somatic_why": "When your upper back (thoracic spine) is stiff from pillows, reading, or looking at a phone, your lower back is forced to overwork. Freeing the shoulder blades against the wall immediately relieves downward pressure on your lumbar vertebrae.",
        "setup": "Stand facing the wall, slightly closer than arm's length. Place your forearms vertically against the wall from elbows to palms at shoulder height.",
        "movement": [
            "Anchor your forearms lightly on the wall, parallel to each other like train tracks.",
            "Step your feet back 6 inches and let your forehead rest gently on the wall between your forearms.",
            "Without moving your elbows, allow your chest to gently sink forward toward the wall for 3 seconds, letting your shoulder blades glide softly together.",
            "Then press lightly through your forearms to round and widen the space between your shoulder blades."
        ],
        "breath": "Inhale for 4 seconds as you widen and separate the shoulder blades. Exhale for 6 seconds as your heart melts softly toward the wall.",
        "feel_good": "Tension melting out of the base of your neck, upper traps, and between the shoulder blades.",
        "avoid": "Shrugging your shoulders up toward your ears or clenching your jaw.",
        "mod_easy": "Keep your feet closer to the wall so almost no weight rests on your forearms.",
        "mod_deep": "Walk your elbows 2 inches higher up the wall to lengthen the triceps and upper lats.",
        "elena_note": "Notice how much tension you unconsciously carry in your shoulders before your first cup of coffee. Let the wall absorb that weight."
    },
    {
        "day": 3,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "Standing L-Traction Hinge",
        "subtitle": "Gravitational L4–L5 Disc Rehydration Protocol",
        "duration": "5 Minutes",
        "sets": "3 Sets × 45 Sec",
        "target": "L4–L5 & Sacrum",
        "pose": "l_traction",
        "somatic_why": "Your lumbar intervertebral discs act like tiny sponges. By creating a supported 90-degree hip hinge with your hands anchored on the wall, you remove vertical gravity compression so nutrient-rich fluid can re-enter stiff lower back discs.",
        "setup": "Place both palms flat on the wall at hip-to-navel height. Walk your feet back until your torso is angled comfortably toward a soft 'L' shape.",
        "movement": [
            "Keep your knees generously soft (bent about 15 degrees) so your hamstrings never pull on your lower back.",
            "Press your palms lightly forward into the wall while imagining someone gently pulling your hips backward with a silk ribbon.",
            "Keep your neck neutral so your ears align naturally between your upper arms.",
            "Sway your hips 1 inch to the right and 1 inch to the left, feeling each side of your lower back release."
        ],
        "breath": "Inhale 4 seconds into your lower back ribs. Exhale 6 seconds as you lengthen your tailbone away from the wall.",
        "feel_good": "A sensation of space opening between the individual vertebrae at your beltline.",
        "avoid": "Locking your knees straight, which triggers hamstring guarding and pulls on the pelvis.",
        "mod_easy": "Keep your hands higher (chest height) and hinge only 45 degrees instead of 90 degrees.",
        "mod_deep": "Inhale to bend both knees slightly deeper, exhale to float the sit-bones gently upward.",
        "elena_note": "Keep those knees soft! A soft knee is the secret key that unlocks a tight lower back."
    },
    {
        "day": 4,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "Wall-Supported Cat-Cow Wave",
        "subtitle": "Segmental Spinal Articulation Without Floor Kneeling",
        "duration": "5 Minutes",
        "sets": "2 Sets × 8 Slow Waves",
        "target": "Full Spine Articulation",
        "pose": "spinal_wave",
        "somatic_why": "Traditional Cat-Cow requires kneeling on hard floors, which crushes sensitive kneecaps. Performing this wave standing at the wall gives you 100% of the synovial spinal lubrication with zero patellar pressure.",
        "setup": "Stand half an arm's length from the wall. Place both palms comfortably on the wall at ribcage height, feet hip-width apart.",
        "movement": [
            "Start at your tailbone: gently tuck your pelvis under, rounding your lower back, mid-back, and finally letting your chin nod toward your chest.",
            "Pause for 2 seconds, feeling the gentle stretch along the back of your spine.",
            "Reverse slowly from the pelvis: tip your tailbone slightly back, let your belly soften, and lift your sternum and gaze softly toward the wall.",
            "Move vertebra by vertebra like a slow ocean wave rather than a stiff hinge."
        ],
        "breath": "Inhale for 4 seconds as your chest opens toward the wall. Exhale for 6 seconds as you round your spine and tuck your tailbone.",
        "feel_good": "A rhythmic, warming wave traveling smoothly up and down your entire spinal column.",
        "avoid": "Throwing your head backward or overarching the lower back into a sharp pinch.",
        "mod_easy": "Make the wave 50% smaller—focus only on the gentle pelvic tuck and release.",
        "mod_deep": "Close your eyes and take 8 full seconds per spinal wave to find sticky spots.",
        "elena_note": "Imagine your spine is a string of pearls lifting and laying down one pearl at a time."
    },
    {
        "day": 5,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "Lateral Ribcage & QL Arc",
        "subtitle": "Side-Waist & Quadratus Lumborum Decompression",
        "duration": "5 Minutes",
        "sets": "45 Sec Per Side × 2",
        "target": "QL Muscle & Side Ribs",
        "pose": "lateral_arc",
        "somatic_why": "80% of 'mysterious' one-sided lower back pain actually comes from a locked Quadratus Lumborum (QL)—the deep muscle connecting your lowest rib to your pelvis. Opening the side body at the wall releases this vise-grip immediately.",
        "setup": "Stand sideways to the wall, about 12 inches away. Place your inside hand or forearm on the wall at shoulder height.",
        "movement": [
            "Keep both feet planted hip-width apart with soft knees.",
            "Sweep your outside arm up and gently curve your torso toward the wall while letting your outer hip drift 2 inches away from the wall.",
            "Create a soft, crescent-moon arc along the outside of your waist and ribcage.",
            "Hold comfortably and breathe directly into the open side of your ribs, then turn around and repeat on the other side."
        ],
        "breath": "Inhale 4 seconds to expand the outer ribs like an accordion. Exhale 6 seconds to soften the waist.",
        "feel_good": "A deep, refreshing yawn-like opening along the side of your waist and outer hip crest.",
        "avoid": "Twisting forward or holding your breath while reaching overhead.",
        "mod_easy": "Rest your outside hand on your hip or ribs instead of reaching overhead.",
        "mod_deep": "Cross your inside ankle slightly in front of your outside ankle for a longer lateral arc.",
        "elena_note": "When you breathe into your side ribs, your diaphragm massages the top of your lower back from the inside out."
    },
    {
        "day": 6,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "Thoracic Open-Book at the Wall",
        "subtitle": "Gentle Rotational Unwinding for Mid-Back & Ribs",
        "duration": "5 Minutes",
        "sets": "6 Slow Opens Per Side",
        "target": "Mid-Back & Rib Mobility",
        "pose": "spinal_wave",
        "somatic_why": "Stiff ribs and mid-back vertebrae force your lower lumbar spine to twist every time you reach into the back seat of a car or turn in kitchen cabinets. Restoring thoracic rotation protects your L4–L5 discs all day long.",
        "setup": "Stand facing the wall, one arm's length away. Place your left palm flat in the center of the wall at shoulder height.",
        "movement": [
            "Keep your hips and knees facing the wall (imagine headlights on your hip bones shining straight ahead).",
            "Inhale as you sweep your right arm open to the right side, following your hand softly with your eyes.",
            "Pause for 3 seconds in your pain-free open position, feeling your chest and mid-back gently rotate.",
            "Exhale as you float your right hand back to meet the wall. Complete 6 slow reps, then switch arms."
        ],
        "breath": "Inhale 4 seconds as you open your arm wide. Exhale 6 seconds as you return smoothly to the wall.",
        "feel_good": "Gentle warmth across your chest, front shoulder, and mid-back ribs.",
        "avoid": "Wrenching your knees or twisting aggressively from your lower waist.",
        "mod_easy": "Place your rotating hand on your breastbone and rotate only your ribs and shoulders.",
        "mod_deep": "Hold the open position for two full 4–6 breath cycles on your final repetition.",
        "elena_note": "Let your eyes lead the movement slowly—where your gaze goes, your spine follows with ease."
    },
    {
        "day": 7,
        "week": 1,
        "week_title": "Week I · Spinal & Lumbar Decompression",
        "title": "The Vagal Breath & Spine Flow",
        "subtitle": "Week 1 Milestone Integration & Nervous System Reset",
        "duration": "5 Minutes",
        "sets": "Continuous 5-Min Flow",
        "target": "Vagus Nerve & Full Spine",
        "pose": "vagal_flow",
        "somatic_why": "You have completed your first 6 days of mechanical decompression. Day 7 cements this new spinal length into your autonomic nervous system by pairing gentle wall support with vagal toning breathwork.",
        "setup": "Stand close to the wall. Stack your palms or forearms on the wall at forehead height and rest your forehead gently against the back of your hands.",
        "movement": [
            "Minute 1–2: Perform 6 slow Wall Palms Presses & Cat-Cow Waves to warm the spine.",
            "Minute 3–5: Rest your forehead on your stacked hands at the wall. Soften your knees, jaw, and belly.",
            "Perform 10 slow 4–6 breath cycles, feeling your entire spine hang Effortlessly from the base of your skull.",
            "Notice how much taller and lighter your lower back feels compared to Day 1."
        ],
        "breath": "4-second nasal inhale into the back of your ribs; 6-second audible sigh exhale through the mouth.",
        "feel_good": "A wave of calm warmth down your neck, shoulders, and lower back—heart rate slowing down.",
        "avoid": "Rushing through the breath count. Give yourself these 5 quiet minutes.",
        "mod_easy": "Perform the breathing phase seated in a chair with your palms resting on the wall in front of you.",
        "mod_deep": "Add a gentle side-to-side sway of your pelvis while your forehead rests on your hands.",
        "elena_note": "Congratulations on completing Week 1! Your spine now knows the wall is a place of relief, not strain."
    },

    # ==================== WEEK 2: HIP LUBRICATION, PSOAS & KNEE RELIEF (DAYS 08 - 14) ====================
    {
        "day": 8,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "Supported Standing Hip Circles",
        "subtitle": "Synovial Fluid Lubrication for Clicking or Stiff Hip Sockets",
        "duration": "5 Minutes",
        "sets": "45 Sec Per Side × 2",
        "target": "Hip Acetabulum (Socket)",
        "pose": "hip_circles",
        "somatic_why": "In Somatic Mobility, we say 'motion is lotion.' The ball-and-socket joint of your hip has no direct blood supply inside the cartilage—it relies on gentle, unloaded circular motion to pump fresh synovial fluid across dry, clicking joint surfaces.",
        "setup": "Stand sideways to the wall. Rest your inside palm flat on the wall at chest height for 100% rock-solid balance.",
        "movement": [
            "Shift your weight onto your inside standing leg, keeping that knee micro-soft.",
            "Lift your outside foot just 2 inches off the floor so the hip joint hangs freely.",
            "Imagine a paintbrush attached to your kneecap: draw 5 slow, coin-sized circles clockwise in the air.",
            "Pause, then draw 5 slow circles counter-clockwise. Turn around and repeat on the other leg."
        ],
        "breath": "Breathe continuously and smoothly (4s in, 6s out)—never hold your breath while balancing.",
        "feel_good": "Smooth, oiled warmth deep inside the hip socket without any popping or catching.",
        "avoid": "Lifting your knee too high (which pinches the hip crease) or hiking your hip bone up.",
        "mod_easy": "Keep your big toe lightly touching the floor as you trace small circles on the ground.",
        "mod_deep": "Close your eyes while holding the wall to heighten your internal joint awareness.",
        "elena_note": "Smaller is smarter! A tiny, buttery-smooth circle lubricates the joint 3x better than a big, clunky circle."
    },
    {
        "day": 9,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "The Wall Pelvic Clock (12-to-6)",
        "subtitle": "Sacroiliac (SI) Joint Reset & Lumbar-Pelvic Rhythm",
        "duration": "5 Minutes",
        "sets": "10 Slow Tilts × 2 Sets",
        "target": "Pelvis, Sacrum & SI Joint",
        "pose": "pelvic_tilt",
        "somatic_why": "Hours of sitting or standing locks your pelvis into an anterior tilt, jamming the sacroiliac (SI) joints at the base of your spine. Using the flat surface of the wall as biofeedback teaches your pelvis to glide smoothly back into neutral alignment.",
        "setup": "Stand with your back to the wall. Rest your shoulder blades and buttocks lightly against the wall, heels walked 4 to 5 inches forward.",
        "movement": [
            "Notice the natural small tunnel of space between your lower back and the wall.",
            "Exhale as you gently tip your pubic bone upward (toward 12 o'clock), imprinting your lower back softly flat against the wall.",
            "Hold this supported imprint for 3 seconds—feel your lower back muscles lengthen.",
            "Inhale as you slowly release your pelvis back to neutral (6 o'clock) without over-arching."
        ],
        "breath": "Exhale for 6 seconds as you flatten your lumbar spine into the wall; inhale for 4 seconds to release.",
        "feel_good": "A deep release across the sacrum (the flat bone above your tailbone) and gentle core awakening.",
        "avoid": "Pushing hard with your legs or squeezing your glutes tightly.",
        "mod_easy": "Place a folded towel behind your head if your neck feels strained against the wall.",
        "mod_deep": "Add '3 o'clock to 9 o'clock' micro-shifts, gently pressing right hip then left hip into the wall.",
        "elena_note": "The wall never lies—it gives your brain instant tactile feedback of where neutral posture truly lives."
    },
    {
        "day": 10,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "Zero-Kneel Standing Psoas Release",
        "subtitle": "Deep Hip Flexor Unwinding Without Touching the Floor",
        "duration": "5 Minutes",
        "sets": "45 Sec Per Side × 2",
        "target": "Iliopsoas & Front Hip",
        "pose": "psoas_release",
        "somatic_why": "Your psoas muscle attaches directly to your lumbar vertebrae (L1–L5) and crosses the front of your hip. When tight from sitting, it yanks your lower back forward every time you stand up. This standing wall variation unlocks the psoas without ever kneeling on a floor lunge.",
        "setup": "Stand facing the wall, hands resting at shoulder height. Step your right foot back into a comfortable, short staggered stance.",
        "movement": [
            "Keep your back heel softly anchored on the floor (or slightly lifted if your calf is tight).",
            "Here is the magic key: before leaning forward, gently tuck your tailbone under (posterior pelvic tilt).",
            "While keeping that subtle tailbone tuck, bend your front knee 2 inches toward the wall.",
            "Stop the exact moment you feel a warm, vertical lengthening down the front of your right hip crease."
        ],
        "breath": "Inhale 4 seconds into your lower belly; exhale 6 seconds and imagine your psoas melting like warm wax.",
        "feel_good": "A clean, vertical opening across the front of the back-leg hip and lower abdomen.",
        "avoid": "Taking a giant lunge step and arching your lower back—that jams the lumbar spine instead of stretching the psoas.",
        "mod_easy": "Take a shorter step back and focus 90% on the gentle tailbone tuck.",
        "mod_deep": "Raise the arm of your back-leg side slightly up the wall to lengthen the entire fascial line.",
        "elena_note": "Remember: the psoas is an emotional muscle connected to your fight-or-flight response. Coax it open gently—never force it."
    },
    {
        "day": 11,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "Outer Hip & Sciatic Pathway Glide",
        "subtitle": "Glute Medius & Piriformis Decompression Against the Wall",
        "duration": "5 Minutes",
        "sets": "45 Sec Per Side × 2",
        "target": "Piriformis & Outer Hip",
        "pose": "lateral_arc",
        "somatic_why": "Deep ache in the side of the hip or radiating tension down the outer leg often comes from a tight piriformis pressing near the sciatic pathway. Gently leaning into the wall releases the lateral hip capsule safely.",
        "setup": "Stand sideways to the wall, about 10 inches away. Place your inside forearm flat against the wall.",
        "movement": [
            "Cross your outside ankle loosely in front of your inside ankle so both feet rest flat on the floor.",
            "Keep your torso upright and gently let your inside hip lean 2 inches toward the wall.",
            "Then slowly shift your hip back to center. Repeat this slow, rhythmic hip-glide 8 times.",
            "On the 8th rep, hold the gentle lean for 3 slow breaths, then switch sides."
        ],
        "breath": "Inhale 4 seconds at center; exhale 6 seconds as you let your hip soften toward the wall.",
        "feel_good": "A deep, satisfying release along the side-glute pocket and outer thigh band.",
        "avoid": "Twisting your knee or collapsing your upper shoulder into the wall.",
        "mod_easy": "Keep your feet uncrossed (parallel hip-width apart) and perform a smaller hip shift.",
        "mod_deep": "Combine with a gentle reach of your outside arm up and over toward the wall.",
        "elena_note": "If you ever feel morning hip bursitis tenderness or sciatic tightness, this gentle glide is your best friend."
    },
    {
        "day": 12,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "Patella Offload & Ankle Glide",
        "subtitle": "Zero-Torque Knee Lubrication & Calf Fascia Release",
        "duration": "5 Minutes",
        "sets": "10 Slow Glides Per Leg",
        "target": "Knee Joint & Ankle",
        "pose": "knee_glide",
        "somatic_why": "When ankles are stiff, your knees are forced to absorb rotational shock with every step you take. By offloading 70% of your bodyweight into your hands on the wall, you can restore ankle and knee glide without grinding the kneecap.",
        "setup": "Stand facing the wall, hands flat at chest height. Step one foot 8 inches forward and the other 8 inches back.",
        "movement": [
            "Transfer generous weight into your palms on the wall so your legs feel light and unloaded.",
            "Keep your front heel glued to the floor and slowly glide your front knee 2 inches forward over your middle toe.",
            "Hold for 2 seconds, feeling the ankle hinge and back calf lengthen while the kneecap tracks smoothly.",
            "Glide smoothly back. Complete 10 slow glides on the right leg, then 10 on the left."
        ],
        "breath": "Inhale 4 seconds as the knee glides forward; exhale 6 seconds as you press back to neutral.",
        "feel_good": "Elastic warmth in the Achilles, calf, and a smooth, creak-free glide around the kneecap.",
        "avoid": "Letting your front knee cave inward toward your big toe.",
        "mod_easy": "Keep the knee bend micro-small (just 1 inch of forward travel) with maximum hand support.",
        "mod_deep": "Pause in the forward glide and lift/lower your toes softly to awaken the shin muscle.",
        "elena_note": "Healthy, pain-free knees start with mobile ankles and hips. Your knees are caught in the middle—today we free them."
    },
    {
        "day": 13,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "Supported Standing Figure-4 Unwind",
        "subtitle": "External Hip Rotator Release Using Wall Stability",
        "duration": "5 Minutes",
        "sets": "40 Sec Per Side × 2",
        "target": "Deep Rotators & Glutes",
        "pose": "hip_circles",
        "somatic_why": "Getting down on the floor for a 'Pigeon pose' is impossible or painful for most women over 45. Using the wall as a vertical backrest lets you open the deep external rotators of the hip while standing safely.",
        "setup": "Stand with your back leaning comfortably against the wall, feet walked 10 inches forward, hip-width apart.",
        "movement": [
            "With your back fully supported by the wall, cross your right ankle gently over your left shin (or just above the left ankle if hips are tight).",
            "Allow your right knee to externally rotate open to the side.",
            "Keep your spine resting flat against the wall—let the wall hold 100% of your balance.",
            "Optionally bend your standing left knee 1 to 2 inches down the wall until you feel a gentle outer-hip release."
        ],
        "breath": "Inhale 4 seconds; exhale 6 seconds as you let the crossed knee soften open without pushing it.",
        "feel_good": "A soothing opening deep in the back pocket of the crossed-leg hip.",
        "avoid": "Pressing down on your knee with your hand or crossing higher than your hip allows comfortably.",
        "mod_easy": "Cross at the low ankle (ankle-over-ankle) with your heel resting on the floor.",
        "mod_deep": "Slide your back 1 inch lower down the wall while keeping your chest tall and relaxed.",
        "elena_note": "Never force the hip open. When your back is supported by the wall, the hip socket opens on its own."
    },
    {
        "day": 14,
        "week": 2,
        "week_title": "Week II · Hip Lubrication, Psoas & Knee Relief",
        "title": "Week 2 Lower-Body Fluidity Flow",
        "subtitle": "Seamless 5-Minute Hip, Pelvis & Knee Integration",
        "duration": "5 Minutes",
        "sets": "Continuous 5-Min Sequence",
        "target": "Hips, Pelvis & Knees",
        "pose": "psoas_release",
        "somatic_why": "Day 14 links your newly lubricated hip sockets, unlocked psoas, and aligned pelvis into a single fluid sequence. Moving smoothly from one position to the next trains your joints to stay mobile when walking and climbing stairs.",
        "setup": "Begin standing sideways to your wall with one hand resting lightly at chest height.",
        "movement": [
            "Minute 1: Supported Standing Hip Circles (30 seconds right leg, 30 seconds left leg).",
            "Minute 2: Turn your back to the wall for 8 slow Wall Pelvic Clock Tilts (12-to-6).",
            "Minute 3–4: Face the wall for the Zero-Kneel Standing Psoas Release (45 seconds each side).",
            "Minute 5: Finish with 6 slow Patella Offload & Ankle Glides per leg."
        ],
        "breath": "Maintain a steady, unhurried 4-second nasal inhale and 6-second mouth exhale throughout all transitions.",
        "feel_good": "Your legs and hips feeling oiled, buoyant, and noticeably lighter when you walk away from the wall.",
        "avoid": "Rushing between positions—treat the transition itself as part of the somatic meditation.",
        "mod_easy": "Take a 15-second standing rest between each 1-minute movement block.",
        "mod_deep": "Walk around your room for 60 seconds afterward and notice the length of your natural stride.",
        "elena_note": "Two full weeks complete! Notice how getting out of bed and rising from chairs already feels different."
    },

    # ==================== WEEK 3: FULL-CHAIN INTEGRATION & LONGEVITY HABIT (DAYS 15 - 21) ====================
    {
        "day": 15,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "The Supported Wall Angels",
        "subtitle": "Postural Re-Alignment for Rounded Shoulders & Upper Spine",
        "duration": "5 Minutes",
        "sets": "2 Sets × 8 Slow Glides",
        "target": "Upper Back, Neck & Chest",
        "pose": "wall_angels",
        "somatic_why": "Gravity slowly pulls our head and shoulders forward over the decades, creating a 'dowager's hump' and compressing the entire spine downward. Wall Angels reverse forward-head posture and open the pectoral fascia in minutes.",
        "setup": "Stand with your back against the wall, feet 5 inches forward. Gently imprint your mid-back and ribs toward the wall.",
        "movement": [
            "Raise your arms to the sides in a soft 'W' or 'Cactus' shape, elbows bent at 90 degrees.",
            "Rest your elbows and the backs of your wrists toward the wall (it is completely normal if they don't touch the wall yet!).",
            "Inhale as you slowly glide your arms 3 to 5 inches upward along the wall.",
            "Exhale as you draw your elbows smoothly back down into your side waist, feeling your lower shoulder blades engage."
        ],
        "breath": "Inhale 4 seconds as arms float up; exhale 6 seconds as elbows glide softly down.",
        "feel_good": "Chest opening wide, collarbones broadening, and your posture instantly feeling 1 inch taller.",
        "avoid": "Popping your lower ribs or arching your lower back off the wall just to force your wrists back.",
        "mod_easy": "Keep your hands 4 inches away from the wall in the air while sliding up and down.",
        "mod_deep": "Keep your lumbar spine softly imprinted against the wall throughout the entire arm glide.",
        "elena_note": "Never sacrifice your lower back just to touch your wrists to the wall. Prioritize a flat, calm ribcage."
    },
    {
        "day": 16,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "Suboccipital & Jaw Tension Release",
        "subtitle": "Cranial-Cervical Alignment & Neck Decompression",
        "duration": "5 Minutes",
        "sets": "2 Sets × 8 Micro-Nods",
        "target": "Cervical Spine & Jaw",
        "pose": "wall_angels",
        "somatic_why": "For every inch your head drifts forward, it adds 10 extra pounds of strain on your neck and lower back. Resetting the tiny suboccipital muscles at the base of your skull relieves tension headaches, neck stiffness, and jaw clenching.",
        "setup": "Stand with your back and the back of your head resting lightly against the wall (place a small folded towel behind your head if needed).",
        "movement": [
            "Keep the back of your head in light contact with the wall.",
            "Perform a tiny 'Yes' micro-nod: gently lengthen the back of your neck up the wall while your chin dips 1 centimeter inward.",
            "Hold for 3 seconds—keep your teeth slightly parted and your tongue resting softly on the roof of your mouth.",
            "Slowly release back to neutral. Repeat 8 gentle times."
        ],
        "breath": "Inhale 4 seconds to prepare; exhale 6 seconds as the back of your neck lengthens upward.",
        "feel_good": "A gentle traction at the very base of your skull where neck tension hides.",
        "avoid": "Jamming your chin down hard into your throat (making a double chin with force).",
        "mod_easy": "Use a 1-inch folded hand towel behind the back of your head so your neck stays effortless.",
        "mod_deep": "Add a slow, 1-inch turn of your nose to the right and left while maintaining the lengthened neck.",
        "elena_note": "Your jaw and your pelvis are neurologically linked. Soften your jaw, and your lower back softens too."
    },
    {
        "day": 17,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "Standing Posterior Fascia Unwind",
        "subtitle": "Hamstring, Calf & Plantar Fascia Release Without Bending Over",
        "duration": "5 Minutes",
        "sets": "45 Sec Per Leg × 2",
        "target": "Hamstrings & Back Line",
        "pose": "l_traction",
        "somatic_why": "Touching your toes from a standing position puts dangerous shear force on aging lumbar discs. By anchoring your hands on the wall and alternating gentle heel-pedals, you release the entire superficial back line safely.",
        "setup": "Face the wall at arm's length. Place both palms flat at chest height and step back into a gentle 60-degree wall hinge.",
        "movement": [
            "Keep your spine long and supported by your hands on the wall.",
            "Slowly bend your right knee while letting your left heel sink heavy into the floor.",
            "Hold for 1 full breath, feeling a gentle lengthening behind your left calf and upper hamstring.",
            "Switch smoothly, pedaling left and right at a slow, meditative tempo for 90 seconds."
        ],
        "breath": "Inhale 4 seconds as you switch legs; exhale 6 seconds as you sink into the heel.",
        "feel_good": "A warm, elastic lengthening from the sole of your foot up the back of your leg.",
        "avoid": "Rounding your lower back or bouncing aggressively into the hamstring.",
        "mod_easy": "Stand closer to the wall so your torso stays almost upright while pedaling the heels.",
        "mod_deep": "Pause on each side and gently lift your toes for 2 seconds to include the plantar fascia.",
        "elena_note": "Your plantar fascia (bottom of the feet), calves, hamstrings, and lower back are one continuous ribbon of tissue."
    },
    {
        "day": 18,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "Cross-Body Somatic Pendulum",
        "subtitle": "Contralateral Shoulder-to-Hip Neuromuscular Slings",
        "duration": "5 Minutes",
        "sets": "8 Slow Swings Per Side",
        "target": "Diagonal Fascial Slings",
        "pose": "hip_circles",
        "somatic_why": "Human walking is a cross-body pattern: your right arm swings with your left leg. Re-coordinating this diagonal fascial sling against the wall restores youthful, effortless grace to your stride.",
        "setup": "Stand sideways to the wall, left hand resting on the wall for balance.",
        "movement": [
            "Stand tall on your left leg with a micro-soft knee.",
            "Gently swing your right leg 4 inches forward while your right arm swings softly backward.",
            "Then let your right leg pendulum 4 inches backward while your right arm floats forward.",
            "Let the limb weight swing like a heavy grandfather clock pendulum—zero muscle forcing."
        ],
        "breath": "Inhale for 2 swings; exhale for 3 swings in a relaxed rhythm.",
        "feel_good": "Effortless momentum lubricating both the shoulder and opposite hip simultaneously.",
        "avoid": "Swinging so high that your torso leans forward or backward.",
        "mod_easy": "Keep the swing tiny (just 2 inches forward and back) and brush your foot lightly on the floor.",
        "mod_deep": "Allow your mid-back ribs to rotate naturally with the gentle arm swing.",
        "elena_note": "Youthful movement isn't about strength—it is about rhythm and coordination."
    },
    {
        "day": 19,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "Morning Joint & Lymphatic Flush",
        "subtitle": "Whole-Body Circulation & Synovial Awakening",
        "duration": "5 Minutes",
        "sets": "3 Rounds × 60 Seconds",
        "target": "Lymphatics & All Joints",
        "pose": "knee_glide",
        "somatic_why": "Unlike your heart, your lymphatic system has no pump—it relies on gentle rhythmic calf contraction and deep diaphragmatic breathing to clear morning puffiness and joint inflammation.",
        "setup": "Stand facing the wall, fingertips or palms resting lightly at chest height, feet hip-width apart.",
        "movement": [
            "Inhale as you rise softly onto the balls of your feet (lifting heels just 1 to 2 inches).",
            "Exhale as you lower your heels softly to the floor and bend your knees 1 inch in a gentle micro-bounce.",
            "Follow immediately with 4 slow Wall Cat-Cow waves.",
            "Finish with 30 seconds of resting your forehead on your hands at the wall."
        ],
        "breath": "Inhale 4 seconds as you rise; exhale 6 seconds as your heels kiss the floor.",
        "feel_good": "A tingling warmth in your feet, calves, hips, and hands—morning sluggishness vanishing.",
        "avoid": "Dropping your heels hard onto the floor or locking your knees at the top.",
        "mod_easy": "Lift your heels only half an inch off the floor while keeping 50% weight in your hands.",
        "mod_deep": "Add a gentle overhead reach of one arm at a time at the top of each heel rise.",
        "elena_note": "Your calves are your 'second heart.' Twenty gentle heel pumps wake up circulation better than espresso."
    },
    {
        "day": 20,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "The Complete 5-Minute Master Flow",
        "subtitle": "Full-Body Dress Rehearsal Linking Spine, Hips & Posture",
        "duration": "5 Minutes",
        "sets": "5 Continuous 1-Min Blocks",
        "target": "Full Somatic Chain",
        "pose": "spinal_wave",
        "somatic_why": "Today we weave the five most powerful movements from Weeks 1, 2, and 3 into a single, seamless 5-minute morning ritual that addresses every major joint from your neck to your ankles.",
        "setup": "Stand at your favorite wall space in comfortable morning clothes, barefoot or in non-slip socks.",
        "movement": [
            "Minute 1 (Spine): Wall Palms Press into 5 slow Standing Cat-Cow Waves.",
            "Minute 2 (Hips): Supported Standing Hip Circles (30 seconds right, 30 seconds left).",
            "Minute 3 (Psoas): Zero-Kneel Standing Psoas Release (30 seconds right, 30 seconds left).",
            "Minute 4 (Posture): Back to the wall for 6 Pelvic Tilts + 6 Supported Wall Angels.",
            "Minute 5 (Nervous System): Forehead resting on hands at the wall for 6 Vagal 4–6 Breaths."
        ],
        "breath": "Let your 4-second inhale and 6-second exhale serve as the metronome for the entire 5 minutes.",
        "feel_good": "Complete head-to-toe decompression, upright posture, and deep nervous system serenity.",
        "avoid": "Checking the clock obsessively—5 or 6 slow breaths per movement equals roughly 1 minute!",
        "mod_easy": "Shorten each block to 4 breaths if you are short on time.",
        "mod_deep": "Add 30 seconds of Lateral Ribcage Arcs on each side if your waist feels tight.",
        "elena_note": "Count in breaths, not seconds! Five slow breaths per movement means you never even need a timer."
    },
    {
        "day": 21,
        "week": 3,
        "week_title": "Week III · Full-Chain Integration & Longevity Habit",
        "title": "Graduation: Your Lifelong Morning Ritual",
        "subtitle": "Cementing Your 5-Minute Daily Freedom Practice Forever",
        "duration": "5 Minutes",
        "sets": "Daily Forever Habit",
        "target": "Lifelong Joint Longevity",
        "pose": "vagal_flow",
        "somatic_why": "Neuroplasticity research shows that 21 consecutive days of gentle sensory-motor input builds a permanent neural pathway. Your brain now associates waking up and touching the wall with immediate joint release and safety.",
        "setup": "Stand at your wall with quiet pride. Take a moment before moving to scan how your back, hips, and knees feel today compared to Day 1.",
        "movement": [
            "Perform your 5-Minute Master Flow (Palms Press → Hip Circles → Psoas Release → Wall Angels → Vagal Breath).",
            "Move at your own intuitive pace, lingering an extra breath on whichever joint asks for extra love today.",
            "After your final exhale, place one hand on your heart and one hand on your lower belly.",
            "Turn to Page 29 to complete your Day 21 Mobility Re-Test and sign your Certificate on Page 30!"
        ],
        "breath": "Deep, effortless 4–6 diaphragmatic breathing—now second nature to your body.",
        "feel_good": "Freedom, pride, fluidity, and confidence in your body's natural ability to heal without pain.",
        "avoid": "Thinking the journey stops here—keep this 5-minute gift before your morning coffee every day.",
        "mod_easy": "On busy mornings, even 60 seconds of the Wall Palms Press keeps the neural pathway alive.",
        "mod_deep": "Repeat the flow in the evening (or pair with the Nighttime Bed Prep Routine on Page 27).",
        "elena_note": "You did it! You proved that your body wasn't broken—it only needed gentleness, support, and 5 minutes a day."
    },
]


def render_daily_page(d: dict, page_num: int) -> str:
    day_num_str = f"{d['day']:02d}"
    svg_illustration = get_posture_svg(d["pose"], d["target"])
    steps_html = "".join(
        f'<li><span class="step-idx">{idx + 1}</span><span>{step}</span></li>'
        for idx, step in enumerate(d["movement"])
    )

    return f"""
  <!-- PAGE {page_num}: DAY {day_num_str} -->
  <section class="page" id="day-{d['day']}">
    <header class="page-header">
      <div class="header-brand">
        <span class="brand-dot"></span>
        <span>COACH ELENA VANCE &bull; THE 21-DAY GENTLE WALL RESET</span>
      </div>
      <span class="header-pill">{d['week_title']}</span>
    </header>

    <!-- Monumental Editorial Day Header -->
    <div class="day-hero">
      <div class="day-num-block">
        <span class="day-label-tiny">DAILY PROTOCOL</span>
        <span class="day-num-giant serif">{day_num_str}</span>
      </div>
      <div class="day-title-block">
        <h2 class="day-title serif">{d['title']}</h2>
        <p class="day-subtitle">{d['subtitle']}</p>
        <div class="meta-strip">
          <span class="meta-chip"><strong>TIME:</strong> {d['duration']}</span>
          <span class="meta-chip"><strong>DOSAGE:</strong> {d['sets']}</span>
          <span class="meta-chip"><strong>TARGET:</strong> {d['target']}</span>
          <span class="meta-chip meta-chip-accent">100% STANDING &bull; ZERO FLOOR</span>
        </div>
      </div>
    </div>

    <!-- Middle 2-Column Editorial Spread: SVG Posture Diagram + Clinical Somatic Why -->
    <div class="day-top-grid">
      <div class="diagram-card">
        <div class="section-kicker">BIOMECHANICAL WALL VECTOR</div>
        {svg_illustration}
      </div>

      <div class="why-column">
        <div class="somatic-why-card">
          <div class="section-kicker">THE SOMATIC WHY &bull; CLINICAL MECHANISM</div>
          <p class="why-text">{d['somatic_why']}</p>
        </div>

        <div class="setup-card">
          <div class="section-kicker">PHASE 1 &bull; WALL SETUP &amp; STANCE</div>
          <p class="setup-text">{d['setup']}</p>
        </div>

        <div class="breath-card">
          <div class="breath-header">
            <span class="section-kicker" style="margin-bottom:0;">PHASE 3 &bull; VAGAL BREATH CADENCE</span>
            <span class="breath-badge">4s IN &middot; 6s OUT</span>
          </div>
          <p class="breath-text">{d['breath']}</p>
        </div>
      </div>
    </div>

    <!-- Step-by-Step Guided Execution -->
    <div class="steps-card">
      <div class="section-kicker">PHASE 2 &bull; STEP-BY-STEP GENTLE EXECUTION</div>
      <ol class="editorial-steps">
        {steps_html}
      </ol>
    </div>

    <!-- Somatic Cues & Modifications Grid (2x2) -->
    <div class="cues-grid">
      <div class="cue-box cue-good">
        <div class="cue-title">
          <span class="cue-icon">&#10003;</span>
          <span>WHAT YOU SHOULD FEEL (GREEN LIGHT)</span>
        </div>
        <p>{d['feel_good']}</p>
      </div>
      <div class="cue-box cue-avoid">
        <div class="cue-title">
          <span class="cue-icon">&times;</span>
          <span>WHAT TO AVOID (GUARDING TRIGGER)</span>
        </div>
        <p>{d['avoid']}</p>
      </div>
      <div class="cue-box cue-mod">
        <div class="cue-title">
          <span>FEATHERLIGHT OPTION (IF EXTRA STIFF TODAY)</span>
        </div>
        <p>{d['mod_easy']}</p>
      </div>
      <div class="cue-box cue-mod">
        <div class="cue-title">
          <span>DEEPER UNWIND PROGRESSION</span>
        </div>
        <p>{d['mod_deep']}</p>
      </div>
    </div>

    <!-- Bottom Bar: Coach Elena's Note + Interactive Daily Somatic Check-In -->
    <div class="day-bottom-bar">
      <div class="elena-note-box">
        <span class="note-label">COACH ELENA'S NOTE</span>
        <p class="serif italic">"{d['elena_note']}"</p>
      </div>
      <div class="checkin-box">
        <div class="checkin-header">
          <span>DAY {day_num_str} CHECK-IN</span>
          <label class="print-check-label">
            <input type="checkbox" class="day-check-input" data-day="{d['day']}" onchange="toggleGuideDay({d['day']}, this.checked)">
            <span class="custom-check-box"></span>
            <span>COMPLETED</span>
          </label>
        </div>
        <div class="checkin-metrics">
          <span>Morning Stiffness: <strong>___ / 10</strong></span>
          <span>Post-Session Ease: <strong>___ / 10</strong></span>
        </div>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Somatic Mobility Protocol</span>
      <span class="page-num-badge">Page {page_num} of 30</span>
    </footer>
  </section>
"""


# Build all 21 daily pages (Pages 5 to 25)
daily_pages_html = ""
for idx, day_item in enumerate(DAYS_DATA):
    daily_pages_html += render_daily_page(day_item, page_num=5 + idx)

# Build Tracker Rows for Pages 28 & 29
tracker_rows_part1 = ""
for d in DAYS_DATA[:11]:
    tracker_rows_part1 += f"""
      <tr>
        <td class="td-day">DAY {d['day']:02d}</td>
        <td><strong>{d['title']}</strong><br><span class="td-sub">{d['target']} &bull; {d['sets']}</span></td>
        <td style="text-align:center;">___ / 10</td>
        <td style="text-align:center;">___ / 10</td>
        <td><div class="notes-line"></div></td>
        <td style="text-align:center;"><span class="tracker-sq"></span></td>
      </tr>
    """

tracker_rows_part2 = ""
for d in DAYS_DATA[11:]:
    tracker_rows_part2 += f"""
      <tr>
        <td class="td-day">DAY {d['day']:02d}</td>
        <td><strong>{d['title']}</strong><br><span class="td-sub">{d['target']} &bull; {d['sets']}</span></td>
        <td style="text-align:center;">___ / 10</td>
        <td style="text-align:center;">___ / 10</td>
        <td><div class="notes-line"></div></td>
        <td style="text-align:center;"><span class="tracker-sq"></span></td>
      </tr>
    """


html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The 21-Day Gentle Wall Reset Guide — Master 30-Page Edition | Coach Elena Vance</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4 portrait;
      margin: 0;
    }}

    :root {{
      --linen: #FAF6F0;
      --sand: #F2ECE1;
      --sand-deep: #E8DFD1;
      --ink: #18221B;
      --ink-soft: #3D4A40;
      --sage: #46594B;
      --sage-light: #647A68;
      --sage-tint: #E9EFEA;
      --terracotta: #B86F4C;
      --terracotta-tint: #F7EBE4;
      --border: #D9CEBE;
      --border-strong: #C2B39E;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--ink);
      background: #E2DBD0;
      font-size: 9.2pt;
      line-height: 1.45;
      -webkit-font-smoothing: antialiased;
    }}

    .serif {{
      font-family: 'Fraunces', Georgia, serif;
    }}
    .italic {{
      font-style: italic;
    }}
    .mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* ========================================================= */
    /* INTERACTIVE WEB TOOLBAR (HIDDEN WHEN PRINTING / PDF)      */
    /* ========================================================= */
    .web-toolbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(24, 34, 27, 0.95);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 10px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      color: #FAF6F0;
      flex-wrap: wrap;
    }}
    .web-toolbar-left {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .web-toolbar-title {{
      font-family: 'Fraunces', serif;
      font-size: 14px;
      font-weight: 600;
      color: #FAF6F0;
    }}
    .web-toolbar-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      background: rgba(184, 111, 76, 0.25);
      border: 1px solid rgba(184, 111, 76, 0.5);
      color: #F3C6B1;
      padding: 2px 8px;
      border-radius: 99px;
    }}
    .web-toolbar-nav {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .web-nav-btn {{
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #E2DBD0;
      font-size: 11px;
      font-weight: 600;
      padding: 5px 11px;
      border-radius: 99px;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .web-nav-btn:hover {{
      background: rgba(255, 255, 255, 0.16);
      color: #FFFFFF;
    }}
    .web-day-select {{
      background: #243328;
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #FAF6F0;
      font-size: 11px;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 99px;
      outline: none;
      cursor: pointer;
    }}
    .web-print-btn {{
      background: #B86F4C;
      color: #FFFFFF;
      border: none;
      font-size: 11px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 99px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
    }}
    .web-print-btn:hover {{
      background: #A35E3D;
    }}

    /* ========================================================= */
    /* A4 EDITORIAL SHEET LAYOUT (EXACT 210mm x 297mm)           */
    /* ========================================================= */
    .page {{
      width: 210mm;
      height: 297mm;
      margin: 18px auto;
      padding: 12mm 14mm 10mm 14mm;
      background: var(--linen);
      box-shadow: 0 16px 40px -10px rgba(24, 34, 27, 0.25);
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      page-break-after: always;
      break-after: page;
    }}
    .page:last-of-type {{
      page-break-after: avoid;
      break-after: auto;
    }}

    /* Subtle Editorial Frame Inside Every Page */
    .page::before {{
      content: '';
      position: absolute;
      inset: 6mm;
      border: 0.75pt solid var(--border);
      pointer-events: none;
      z-index: 0;
    }}

    .page > * {{
      position: relative;
      z-index: 1;
    }}

    @media print {{
      body {{
        background: var(--linen);
      }}
      .web-toolbar {{
        display: none !important;
      }}
      .page {{
        margin: 0;
        box-shadow: none;
        width: 210mm;
        height: 297mm;
      }}
    }}

    /* ========================================================= */
    /* HEADERS & FOOTERS                                         */
    /* ========================================================= */
    .page-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1pt solid var(--border-strong);
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}
    .header-brand {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.2pt;
      font-weight: 600;
      letter-spacing: 0.08em;
      color: var(--sage);
    }}
    .brand-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--terracotta);
      display: inline-block;
    }}
    .header-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      font-weight: 600;
      color: var(--ink);
      background: var(--sand);
      border: 0.75pt solid var(--border-strong);
      padding: 2px 9px;
      border-radius: 99px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .page-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 0.75pt solid var(--border);
      padding-top: 5px;
      margin-top: auto;
      font-size: 7.2pt;
      color: var(--sage-light);
      font-family: 'JetBrains Mono', monospace;
    }}
    .page-num-badge {{
      color: var(--ink);
      font-weight: 600;
    }}

    /* ========================================================= */
    /* PAGE 1: COVER PAGE                                        */
    /* ========================================================= */
    .cover-inner {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      padding: 8mm 8mm 4mm 8mm;
      border: 0.75pt solid var(--border-strong);
      margin: 2mm;
      background: linear-gradient(180deg, #FAF6F0 0%, #F3ECE0 100%);
    }}
    .cover-edition-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      font-weight: 600;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--terracotta);
      background: var(--terracotta-tint);
      border: 0.75pt solid #E2BFA8;
      padding: 5px 14px;
      border-radius: 99px;
      margin-bottom: 10px;
    }}
    .cover-main-title {{
      font-size: 31pt;
      line-height: 1.08;
      color: var(--ink);
      font-weight: 600;
      letter-spacing: -0.02em;
      margin-bottom: 10px;
    }}
    .cover-main-sub {{
      font-size: 10.5pt;
      color: var(--ink-soft);
      max-width: 430px;
      margin: 0 auto;
      line-height: 1.5;
    }}
    .cover-arch-frame {{
      width: 165px;
      height: 205px;
      border-radius: 90px 90px 14px 14px;
      overflow: hidden;
      border: 2pt solid var(--sage);
      box-shadow: 0 12px 28px -8px rgba(24, 34, 27, 0.22);
      margin: 12px auto 10px auto;
      background: var(--sand);
      padding: 4px;
    }}
    .cover-arch-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 86px 86px 10px 10px;
    }}
    .cover-metrics-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      width: 100%;
      margin: 10px 0;
    }}
    .cover-metric-card {{
      background: var(--linen);
      border: 0.75pt solid var(--border-strong);
      border-radius: 8px;
      padding: 8px 6px;
    }}
    .cover-metric-val {{
      font-family: 'Fraunces', serif;
      font-size: 13pt;
      font-weight: 700;
      color: var(--sage);
      display: block;
    }}
    .cover-metric-lbl {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.5pt;
      text-transform: uppercase;
      color: var(--ink-soft);
      letter-spacing: 0.05em;
    }}

    /* ========================================================= */
    /* DAILY PAGE COMPONENTS                                     */
    /* ========================================================= */
    .day-hero {{
      display: flex;
      align-items: center;
      gap: 14px;
      background: var(--sand);
      border: 0.75pt solid var(--border-strong);
      border-radius: 10px;
      padding: 9px 14px;
      margin-bottom: 8px;
    }}
    .day-num-block {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding-right: 14px;
      border-right: 1pt solid var(--border-strong);
      min-width: 68px;
    }}
    .day-label-tiny {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6pt;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--terracotta);
    }}
    .day-num-giant {{
      font-size: 27pt;
      font-weight: 700;
      line-height: 0.95;
      color: var(--ink);
    }}
    .day-title-block {{
      flex: 1;
    }}
    .day-title {{
      font-size: 15.5pt;
      font-weight: 700;
      color: var(--ink);
      line-height: 1.15;
    }}
    .day-subtitle {{
      font-size: 8.8pt;
      color: var(--ink-soft);
      margin-bottom: 6px;
    }}
    .meta-strip {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }}
    .meta-chip {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.6pt;
      background: var(--linen);
      border: 0.75pt solid var(--border);
      padding: 2px 7px;
      border-radius: 4px;
      color: var(--ink-soft);
    }}
    .meta-chip-accent {{
      background: var(--sage-tint);
      border-color: #B8C9BC;
      color: var(--sage);
      font-weight: 700;
    }}

    .section-kicker {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.6pt;
      font-weight: 700;
      letter-spacing: 0.09em;
      text-transform: uppercase;
      color: var(--terracotta);
      margin-bottom: 4px;
    }}

    .day-top-grid {{
      display: grid;
      grid-template-columns: 42% 58%;
      gap: 10px;
      margin-bottom: 8px;
      padding-right: 10px;
    }}
    .diagram-card {{
      background: var(--sand);
      border: 0.75pt solid var(--border);
      border-radius: 10px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .posture-svg {{
      width: 100%;
      height: auto;
      display: block;
    }}
    .why-column {{
      display: flex;
      flex-direction: column;
      gap: 7px;
      justify-content: space-between;
    }}
    .somatic-why-card {{
      background: var(--linen);
      border: 0.75pt solid var(--border-strong);
      border-left: 3pt solid var(--sage);
      border-radius: 8px;
      padding: 7px 10px;
    }}
    .why-text, .setup-text, .breath-text {{
      font-size: 8.4pt;
      color: var(--ink-soft);
      line-height: 1.42;
    }}
    .setup-card {{
      background: var(--sand);
      border: 0.75pt solid var(--border);
      border-radius: 8px;
      padding: 7px 10px;
    }}
    .breath-card {{
      background: var(--sage-tint);
      border: 0.75pt solid #B8C9BC;
      border-radius: 8px;
      padding: 7px 10px;
    }}
    .breath-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }}
    .breath-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.5pt;
      font-weight: 700;
      background: var(--sage);
      color: #FFFFFF;
      padding: 1px 6px;
      border-radius: 4px;
    }}

    /* Step-by-Step Card */
    .steps-card {{
      background: #FFFFFF;
      border: 0.75pt solid var(--border-strong);
      border-radius: 10px;
      padding: 8px 12px;
      margin-bottom: 8px;
    }}
    .editorial-steps {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 5px;
      margin-top: 4px;
    }}
    .editorial-steps li {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 8.6pt;
      color: var(--ink);
      line-height: 1.38;
    }}
    .step-idx {{
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--sage);
      color: #FAF6F0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
    }}

    /* Cues & Modifications 2x2 Grid */
    .cues-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
      margin-bottom: 8px;
    }}
    .cue-box {{
      border-radius: 8px;
      padding: 6.5px 9px;
      font-size: 8pt;
      line-height: 1.35;
    }}
    .cue-title {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.5pt;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .cue-good {{
      background: #EDF3EE;
      border: 0.75pt solid #B8C9BC;
      color: #1F3525;
    }}
    .cue-good .cue-title {{ color: #2D5A39; }}
    .cue-avoid {{
      background: #F9EFEA;
      border: 0.75pt solid #E2BFA8;
      color: #4A2818;
    }}
    .cue-avoid .cue-title {{ color: #9E4722; }}
    .cue-mod {{
      background: var(--sand);
      border: 0.75pt solid var(--border);
      color: var(--ink-soft);
    }}
    .cue-mod .cue-title {{ color: var(--sage); }}

    /* Bottom Note + Daily Check-in */
    .day-bottom-bar {{
      display: grid;
      grid-template-columns: 60% 40%;
      gap: 8px;
      padding-right: 8px;
      margin-bottom: 4px;
    }}
    .elena-note-box {{
      background: var(--terracotta-tint);
      border: 0.75pt solid #E2BFA8;
      border-left: 3pt solid var(--terracotta);
      border-radius: 8px;
      padding: 6px 10px;
    }}
    .note-label {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.2pt;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--terracotta);
      display: block;
      margin-bottom: 2px;
    }}
    .elena-note-box p {{
      font-size: 8.3pt;
      color: var(--ink);
      line-height: 1.35;
    }}
    .checkin-box {{
      background: #FFFFFF;
      border: 0.75pt solid var(--border-strong);
      border-radius: 8px;
      padding: 6px 9px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .checkin-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.6pt;
      font-weight: 700;
      color: var(--sage);
      border-bottom: 0.5pt dashed var(--border);
      padding-bottom: 4px;
    }}
    .print-check-label {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      color: var(--ink);
    }}
    .day-check-input {{
      width: 11px;
      height: 11px;
      accent-color: var(--sage);
    }}
    .checkin-metrics {{
      display: flex;
      justify-content: space-between;
      font-size: 7.4pt;
      color: var(--ink-soft);
      padding-top: 4px;
    }}

    /* Intro & Bonus Shared Blocks */
    .editorial-box {{
      background: var(--sand);
      border: 0.75pt solid var(--border-strong);
      border-radius: 10px;
      padding: 11px 14px;
      margin-bottom: 9px;
    }}
    .editorial-box-white {{
      background: #FFFFFF;
      border: 0.75pt solid var(--border-strong);
      border-radius: 10px;
      padding: 11px 14px;
      margin-bottom: 9px;
    }}
    .week-overview-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 9px;
      margin: 8px 0;
    }}
    .week-col-card {{
      background: #FFFFFF;
      border: 0.75pt solid var(--border-strong);
      border-top: 3pt solid var(--sage);
      border-radius: 8px;
      padding: 9px 10px;
    }}
    .week-col-card h4 {{
      font-family: 'Fraunces', serif;
      font-size: 10.5pt;
      color: var(--ink);
      margin-bottom: 4px;
    }}
    .week-day-list {{
      list-style: none;
      font-size: 7.6pt;
      color: var(--ink-soft);
      line-height: 1.55;
    }}

    /* Tracker Table (Pages 28 & 29) */
    .tracker-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8pt;
      background: #FFFFFF;
      border: 0.75pt solid var(--border-strong);
    }}
    .tracker-table th {{
      background: var(--ink);
      color: var(--linen);
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.8pt;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 6px 8px;
      text-align: left;
    }}
    .tracker-table td {{
      padding: 5.5px 8px;
      border-bottom: 0.5pt solid var(--border);
      color: var(--ink);
    }}
    .tracker-table tr:nth-child(even) {{
      background: var(--sand);
    }}
    .td-day {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--terracotta);
      width: 58px;
    }}
    .td-sub {{
      font-size: 7pt;
      color: var(--ink-soft);
    }}
    .notes-line {{
      border-bottom: 0.5pt dashed var(--border-strong);
      height: 12px;
      width: 100%;
    }}
    .tracker-sq {{
      display: inline-block;
      width: 13px;
      height: 13px;
      border: 1.2pt solid var(--sage);
      border-radius: 3px;
      background: #FFFFFF;
    }}
  </style>
</head>
<body>

  <!-- INTERACTIVE WEB NAVIGATION BAR (Hidden in PDF Print) -->
  <nav class="web-toolbar">
    <div class="web-toolbar-left">
      <span class="web-toolbar-title">The 21-Day Gentle Wall Reset</span>
      <span class="web-toolbar-badge">30-PAGE MASTER EDITION</span>
    </div>
    <div class="web-toolbar-nav">
      <a href="#page-cover" class="web-nav-btn">Cover</a>
      <a href="#page-science" class="web-nav-btn">Science &amp; Rules</a>
      <a href="#day-1" class="web-nav-btn">Week 1 (Days 1–7)</a>
      <a href="#day-8" class="web-nav-btn">Week 2 (Days 8–14)</a>
      <a href="#day-15" class="web-nav-btn">Week 3 (Days 15–21)</a>
      <a href="#page-bonus-1" class="web-nav-btn">Bonuses</a>
      <a href="#page-tracker-1" class="web-nav-btn">21D Tracker</a>
      <select class="web-day-select" onchange="if(this.value) location.hash=this.value">
        <option value="">Jump to Day (01–21)...</option>
        {"".join(f'<option value="#day-{d["day"]}">Day {d["day"]:02d}: {d["title"]}</option>' for d in DAYS_DATA)}
      </select>
      <a href="The_21_Day_Gentle_Wall_Reset_Guide.pdf" download class="web-print-btn">
        <span>Download PDF (30 Pages)</span>
      </a>
    </div>
  </nav>

  <!-- ========================================================= -->
  <!-- PAGE 1: EDITORIAL COVER PAGE                              -->
  <!-- ========================================================= -->
  <section class="page" id="page-cover">
    <div class="cover-inner">
      <div>
        <div class="cover-edition-pill">
          <span>OFFICIAL SOMATIC MOBILITY ATLAS</span>
          <span>&bull;</span>
          <span>REVISED 30-PAGE EDITION</span>
        </div>
        <h1 class="cover-main-title serif">The 21-Day Gentle<br><span class="italic" style="color: var(--sage);">Wall Reset</span> Guide</h1>
        <p class="cover-main-sub">
          A Day-by-Day Standing Somatic Decompression Protocol for Women 45+ to Unlock Stiff Lower Backs, Lubricate Clicking Hips &amp; Free Sensitive Knees—With Zero Floor Work.
        </p>
      </div>

      <div>
        <div class="cover-arch-frame">
          <img class="cover-arch-img" src="data:image/jpeg;base64,{hero_b64}" alt="Coach Elena Vance">
        </div>
        <div class="serif" style="font-size: 13.5pt; font-weight: 700; color: var(--ink);">Coach Elena Vance</div>
        <div class="mono" style="font-size: 7.2pt; color: var(--sage); letter-spacing: 0.08em; text-transform: uppercase; margin-top: 2px;">
          Somatic Mobility &amp; Joint Decompression Specialist &bull; @coach.elena.vance
        </div>
      </div>

      <div style="width: 100%;">
        <div class="cover-metrics-grid">
          <div class="cover-metric-card">
            <span class="cover-metric-val">21 Days</span>
            <span class="cover-metric-lbl">1 Page Per Day</span>
          </div>
          <div class="cover-metric-card">
            <span class="cover-metric-val">5 Min</span>
            <span class="cover-metric-lbl">Morning Ritual</span>
          </div>
          <div class="cover-metric-card">
            <span class="cover-metric-val">100%</span>
            <span class="cover-metric-lbl">Standing At Wall</span>
          </div>
          <div class="cover-metric-card">
            <span class="cover-metric-val">Zero</span>
            <span class="cover-metric-lbl">Floor Kneeling</span>
          </div>
        </div>

        <div class="mono" style="font-size: 6.8pt; color: var(--ink-soft); border-top: 0.75pt solid var(--border-strong); padding-top: 8px; display: flex; justify-content: space-between;">
          <span>ELENA VANCE STUDIO PRESS &bull; NEW YORK / MADRID</span>
          <span>PERSONAL DIGITAL &amp; PRINT EDITION</span>
          <span>PAGE 1 OF 30</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 2: WELCOME LETTER & 21-DAY MASTER SYLLABUS           -->
  <!-- ========================================================= -->
  <section class="page" id="page-welcome">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Preface &amp; Master Curriculum</span>
    </header>

    <div>
      <div class="section-kicker">A PERSONAL LETTER FROM COACH ELENA VANCE</div>
      <h2 class="serif" style="font-size: 19pt; color: var(--ink); margin-bottom: 8px;">"Your Body Isn't Broken—It Is Waiting to Feel Safe."</h2>

      <div class="editorial-box" style="border-left: 3pt solid var(--terracotta); background: var(--terracotta-tint);">
        <p class="serif italic" style="font-size: 10pt; color: var(--ink); line-height: 1.5;">
          "If you wake up feeling like your lower back is poured in concrete, your hips click when rising from a chair, or your knees ache on the stairs—you have likely been told it is 'just aging.' That is a myth. What you are feeling is an involuntary nervous system guarding reflex. Over the next 21 days, using nothing but your living room wall and 5 quiet minutes each morning, we are going to switch that alarm off."
        </p>
      </div>

      <p style="font-size: 8.9pt; color: var(--ink-soft); margin-bottom: 10px; line-height: 1.52;">
        Mainstream fitness was designed for 25-year-old athletes. When a woman over 45 gets down on a hard floor for planks, lunges, or aggressive stretches, her brain detects joint instability and triggers <strong>protective muscular co-contraction</strong>—locking the psoas, lumbar fascia, and hip sockets even tighter. By standing upright and offloading gravity into a sturdy wall, your brain registers instant mechanical safety. Within 60 seconds, synovial fluid begins lubricating dry cartilage and compressed spinal discs rehydrate naturally.
      </p>

      <div class="section-kicker" style="margin-top: 6px;">COMPLETE 21-DAY ARCHITECTURAL SYLLABUS (PAGES 5 TO 25)</div>
      <div class="week-overview-grid">
        <div class="week-col-card">
          <div class="section-kicker">DAYS 01 &ndash; 07</div>
          <h4>Week I: Spinal &amp; Lumbar Decompression</h4>
          <ul class="week-day-list">
            <li><strong>Day 01:</strong> The Wall Palms Press</li>
            <li><strong>Day 02:</strong> Scapular Wall Melt</li>
            <li><strong>Day 03:</strong> Standing L-Traction Hinge</li>
            <li><strong>Day 04:</strong> Wall-Supported Cat-Cow Wave</li>
            <li><strong>Day 05:</strong> Lateral Ribcage &amp; QL Arc</li>
            <li><strong>Day 06:</strong> Thoracic Open-Book</li>
            <li><strong>Day 07:</strong> Vagal Breath &amp; Spine Flow</li>
          </ul>
        </div>
        <div class="week-col-card" style="border-top-color: var(--terracotta);">
          <div class="section-kicker">DAYS 08 &ndash; 14</div>
          <h4>Week II: Hip Sockets, Psoas &amp; Knees</h4>
          <ul class="week-day-list">
            <li><strong>Day 08:</strong> Supported Hip Micro-Circles</li>
            <li><strong>Day 09:</strong> Wall Pelvic Clock (12-to-6)</li>
            <li><strong>Day 10:</strong> Zero-Kneel Psoas Release</li>
            <li><strong>Day 11:</strong> Outer Hip &amp; Sciatic Glide</li>
            <li><strong>Day 12:</strong> Patella Offload &amp; Ankle Glide</li>
            <li><strong>Day 13:</strong> Supported Standing Figure-4</li>
            <li><strong>Day 14:</strong> Lower-Body Fluidity Flow</li>
          </ul>
        </div>
        <div class="week-col-card">
          <div class="section-kicker">DAYS 15 &ndash; 21</div>
          <h4>Week III: Posture &amp; Lifelong Ritual</h4>
          <ul class="week-day-list">
            <li><strong>Day 15:</strong> Supported Wall Angels</li>
            <li><strong>Day 16:</strong> Suboccipital &amp; Jaw Release</li>
            <li><strong>Day 17:</strong> Posterior Fascia Unwind</li>
            <li><strong>Day 18:</strong> Cross-Body Somatic Pendulum</li>
            <li><strong>Day 19:</strong> Morning Joint &amp; Lymph Flush</li>
            <li><strong>Day 20:</strong> Complete 5-Min Master Flow</li>
            <li><strong>Day 21:</strong> Lifelong Morning Graduation</li>
          </ul>
        </div>
      </div>

      <div class="editorial-box-white" style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
        <div>
          <div class="section-kicker" style="margin-bottom:2px;">INCLUDED BONUSES &amp; CLINICAL LOGS (PAGES 26 TO 30)</div>
          <p style="font-size: 8.4pt; color: var(--ink-soft);">
            <strong>Page 26:</strong> Bonus #1 (30-Sec Car &amp; Desk Emergency Fix) &bull;
            <strong>Page 27:</strong> Bonus #2 (Nighttime Bed Prep Routine) &bull;
            <strong>Pages 28–29:</strong> 21-Day Habit Tracker &bull;
            <strong>Page 30:</strong> Graduation Certificate.
          </p>
        </div>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Somatic Mobility Protocol</span>
      <span class="page-num-badge">Page 2 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 3: SOMATIC SCIENCE & THE 4 GOLDEN RULES              -->
  <!-- ========================================================= -->
  <section class="page" id="page-science">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Biomechanics &amp; Golden Rules</span>
    </header>

    <div>
      <div class="section-kicker">NEURO-BIOMECHANICS OF SOMATIC WALL MOBILITY</div>
      <h2 class="serif" style="font-size: 18pt; color: var(--ink); margin-bottom: 8px;">Why The Wall Unlocks Joints That Floor Stretching Tightens</h2>

      <!-- Custom SVG Comparison Diagram -->
      <div class="editorial-box-white" style="padding: 10px 12px;">
        <svg viewBox="0 0 500 125" style="width: 100%; height: auto; display: block;" xmlns="http://www.w3.org/2000/svg">
          <!-- Left Box: Traditional Floor Stretching -->
          <rect x="4" y="4" width="236" height="117" rx="8" fill="#F9EFEA" stroke="#E2BFA8" stroke-width="1"/>
          <text x="18" y="22" font-family="JetBrains Mono, monospace" font-size="7.5" font-weight="700" fill="#9E4722">TRADITIONAL FLOOR STRETCHING (HIGH CORTISOL)</text>
          <line x1="18" y1="88" x2="220" y2="88" stroke="#9E4722" stroke-width="1.5"/>
          <circle cx="62" cy="56" r="8" fill="#FAF6F0" stroke="#4A2818" stroke-width="1.6"/>
          <path d="M70 60 Q105 42 135 72 L165 87 L195 87" fill="none" stroke="#4A2818" stroke-width="2.2" stroke-linecap="round"/>
          <circle cx="135" cy="72" r="9" fill="#9E4722" fill-opacity="0.25" stroke="#9E4722" stroke-width="1.2" stroke-dasharray="2 2"/>
          <text x="18" y="106" font-family="Plus Jakarta Sans, sans-serif" font-size="7.5" fill="#4A2818">&times; Knee compression &amp; balance strain trigger muscle lock</text>

          <!-- Right Box: Somatic Wall Offloading -->
          <rect x="260" y="4" width="236" height="117" rx="8" fill="#EDF3EE" stroke="#B8C9BC" stroke-width="1"/>
          <text x="274" y="22" font-family="JetBrains Mono, monospace" font-size="7.5" font-weight="700" fill="#2D5A39">ELENA'S WALL RESET METHOD (VAGAL SAFETY)</text>
          <rect x="276" y="30" width="8" height="60" rx="2" fill="#D9CEBE" stroke="#46594B" stroke-width="1.2"/>
          <line x1="272" y1="90" x2="480" y2="90" stroke="#2D5A39" stroke-width="1.5"/>
          <circle cx="332" cy="42" r="8" fill="#FAF6F0" stroke="#18221B" stroke-width="1.6"/>
          <line x1="326" y1="54" x2="285" y2="56" stroke="#18221B" stroke-width="2" stroke-linecap="round"/>
          <line x1="332" y1="50" x2="336" y2="89" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
          <circle cx="334" cy="68" r="9" fill="#46594B" fill-opacity="0.22" stroke="#2D5A39" stroke-width="1.2"/>
          <text x="362" y="54" font-family="JetBrains Mono, monospace" font-size="7" font-weight="700" fill="#2D5A39">70% GRAVITY OFF-LOAD</text>
          <text x="362" y="66" font-family="Plus Jakarta Sans, sans-serif" font-size="7" fill="#1F3525">Discs rehydrate &amp; psoas melts</text>
          <text x="274" y="106" font-family="Plus Jakarta Sans, sans-serif" font-size="7.5" fill="#1F3525">&#10003; 100% upright stability dissolves protective tension</text>
        </svg>
      </div>

      <div class="section-kicker" style="margin-top: 6px;">THE 4 GOLDEN RULES OF YOUR MORNING WALL RITUAL</div>
      <div class="cues-grid" style="margin-bottom: 10px;">
        <div class="editorial-box" style="margin-bottom:0;">
          <div class="section-kicker">RULE 01 &bull; THE 60% EFFORT LAW</div>
          <p style="font-size: 8.3pt; color: var(--ink-soft);">
            Never stretch to a 9/10 intensity. Move only to <strong>60% of your range</strong>—where you feel a whisper of lengthening and zero pinching. Somatic release happens when the brain feels unthreatened.
          </p>
        </div>
        <div class="editorial-box" style="margin-bottom:0;">
          <div class="section-kicker">RULE 02 &bull; MICRO-SOFT KNEES ALWAYS</div>
          <p style="font-size: 8.3pt; color: var(--ink-soft);">
            Locking your knees pulls tightly on the sciatic nerve and hamstrings. Keep a <strong>5-degree 'velvet softness'</strong> behind your knees on every standing movement.
          </p>
        </div>
        <div class="editorial-box" style="margin-bottom:0;">
          <div class="section-kicker">RULE 03 &bull; THE 4–6 VAGAL EXHALE</div>
          <p style="font-size: 8.3pt; color: var(--ink-soft);">
            Inhale through your nose for <strong>4 seconds</strong>; exhale softly through parted lips for <strong>6 seconds</strong>. A longer exhale stimulates the vagus nerve and lowers muscle tone within 3 breaths.
          </p>
        </div>
        <div class="editorial-box" style="margin-bottom:0;">
          <div class="section-kicker">RULE 04 &bull; HABIT STACKING AT THE WALL</div>
          <p style="font-size: 8.3pt; color: var(--ink-soft);">
            Anchor your 5 minutes to an existing habit: perform your daily page <strong>while your morning coffee brews</strong> or right after brushing your teeth. No workout clothes needed.
          </p>
        </div>
      </div>

      <!-- Visual Vagal Breath Cadence Bar -->
      <div class="breath-card" style="padding: 10px 14px;">
        <div class="breath-header">
          <span class="section-kicker" style="margin-bottom:0;">VISUAL VAGAL BREATH PACER (USE THIS RHYTHM ON EVERY PAGE)</span>
          <span class="breath-badge">6 BREATHS = 1 MINUTE</span>
        </div>
        <p style="font-size: 8.3pt; color: var(--ink); margin-top: 4px;">
          You never need a stopwatch while practicing. Simply count <strong>6 slow breath cycles</strong> (4 seconds in + 6 seconds out = 10 seconds per breath). Six calm breaths equal exactly <strong>60 seconds of somatic release</strong>.
        </p>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Somatic Mobility Protocol</span>
      <span class="page-num-badge">Page 3 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 4: DAY 0 BASELINE MOBILITY CHECK                     -->
  <!-- ========================================================= -->
  <section class="page" id="page-baseline">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Day 0 Baseline Assessment</span>
    </header>

    <div>
      <div class="section-kicker">PRE-RESET SOMATIC BENCHMARK</div>
      <h2 class="serif" style="font-size: 18pt; color: var(--ink); margin-bottom: 6px;">Your 3-Minute Standing Wall Self-Check (Before Day 1)</h2>
      <p style="font-size: 8.8pt; color: var(--ink-soft); margin-bottom: 10px;">
        Before beginning Day 01, perform these three gentle checks standing against your wall. Record your honest baseline below so you can celebrate your measurable progress on Day 7, Day 14, and Day 21.
      </p>

      <div class="editorial-box-white">
        <div class="section-kicker">TEST 01 &bull; THE OCCIPUT &amp; SACRUM WALL ALIGNMENT CHECK</div>
        <p style="font-size: 8.5pt; color: var(--ink-soft); margin-bottom: 6px;">
          Stand with your heels 4 inches from the wall, letting your buttocks and upper back touch the wall naturally. Notice where your head and lower back sit without forcing them:
        </p>
        <div class="meta-strip">
          <span class="meta-chip">[ &nbsp; ] Head touches wall easily</span>
          <span class="meta-chip">[ &nbsp; ] Chin tilts up / neck feels tight</span>
          <span class="meta-chip">[ &nbsp; ] Lower back arch feels jammed</span>
        </div>
      </div>

      <div class="editorial-box-white">
        <div class="section-kicker">TEST 02 &bull; OVERHEAD SHOULDER &amp; RIBCAGE GLIDE</div>
        <p style="font-size: 8.5pt; color: var(--ink-soft); margin-bottom: 6px;">
          Staying against the wall, raise both arms into a 'Cactus / W' shape. Notice how close your elbows and wrists come to the wall without your lower ribs popping forward:
        </p>
        <div class="meta-strip">
          <span class="meta-chip">[ &nbsp; ] Wrists &amp; elbows touch wall</span>
          <span class="meta-chip">[ &nbsp; ] Wrists 2–4 inches from wall</span>
          <span class="meta-chip">[ &nbsp; ] Pinching or tightness in front chest</span>
        </div>
      </div>

      <div class="editorial-box-white">
        <div class="section-kicker">TEST 03 &bull; SINGLE-LEG SUPPORTED HIP LIFT</div>
        <p style="font-size: 8.5pt; color: var(--ink-soft); margin-bottom: 6px;">
          Stand sideways with one hand on the wall. Gently lift your outside knee 3 inches off the floor and make one slow circle:
        </p>
        <div class="meta-strip">
          <span class="meta-chip">[ &nbsp; ] Smooth &amp; silent motion</span>
          <span class="meta-chip">[ &nbsp; ] Audible hip clicking / popping</span>
          <span class="meta-chip">[ &nbsp; ] Heavy or stiff in front hip crease</span>
        </div>
      </div>

      <!-- Baseline vs Day 21 Comparison Table -->
      <div class="editorial-box" style="margin-top: 10px;">
        <div class="section-kicker">YOUR PERSONAL MOBILITY TRANSFORMATION SCORECARD (RATE 1 = PAIN/STIFF TO 10 = EFFORTLESS)</div>
        <table class="tracker-table" style="margin-top: 6px;">
          <thead>
            <tr>
              <th>Somatic Biomarker</th>
              <th style="text-align:center;">Day 0 Baseline</th>
              <th style="text-align:center;">Day 7 Check</th>
              <th style="text-align:center;">Day 14 Check</th>
              <th style="text-align:center;">Day 21 Final</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Morning First-Step Lower Back Ease</strong></td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
            </tr>
            <tr>
              <td><strong>Hip Comfort Rising from Chairs / Car</strong></td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
            </tr>
            <tr>
              <td><strong>Knee Confidence on Stairs</strong></td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
            </tr>
            <tr>
              <td><strong>Upright Posture &amp; Neck Lightness</strong></td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
              <td style="text-align:center;">___ / 10</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Somatic Mobility Protocol</span>
      <span class="page-num-badge">Page 4 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGES 5 TO 25: THE 21 DAILY PROTOCOLS (1 PAGE PER DAY)    -->
  <!-- ========================================================= -->
  {daily_pages_html}

  <!-- ========================================================= -->
  <!-- PAGE 26: BONUS #1 — 30-SEC CAR & DESK EMERGENCY SHEET     -->
  <!-- ========================================================= -->
  <section class="page" id="page-bonus-1">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Bonus Protocol #1</span>
    </header>

    <div>
      <div class="section-kicker">EXCLUSIVE QUICK-RELIEF CHEAT SHEET</div>
      <h2 class="serif" style="font-size: 19pt; color: var(--ink); margin-bottom: 4px;">The 30-Second Car, Desk &amp; Travel Emergency Fix</h2>
      <p style="font-size: 8.8pt; color: var(--ink-soft); margin-bottom: 10px;">
        Whenever you sit for more than 45 minutes in a car, airplane, or office chair, your hip flexors shorten into a 'seated cast' and your lumbar discs compress by up to 30%. Perform this 3-step micro-sequence at the nearest wall or doorway within 60 seconds of standing up.
      </p>

      <div class="day-top-grid">
        <div class="diagram-card">
          <div class="section-kicker">30-SECOND DOORWAY / WALL UNLOCK</div>
          {get_posture_svg("psoas_release", "INSTANTPSOAS UNLOCK")}
        </div>
        <div class="why-column">
          <div class="editorial-box-white" style="margin-bottom:0;">
            <div class="section-kicker">SECOND 00 TO 10 &bull; THE TAILBONE UN-TUCK</div>
            <p style="font-size: 8.4pt; color: var(--ink-soft);">
              Place both hands on any wall, car roof, or doorframe at shoulder height. Step one foot back, keep knees soft, and gently tuck your tailbone under for 1 full 4–6 breath to tell your psoas it is no longer sitting.
            </p>
          </div>
          <div class="editorial-box-white" style="margin-bottom:0;">
            <div class="section-kicker">SECOND 10 TO 20 &bull; THE L4–L5 TRACTION HINGE</div>
            <p style="font-size: 8.4pt; color: var(--ink-soft);">
              Step both feet back into a gentle 45-degree wall hinge. Let your chest soften downward while your sit-bones reach back, creating immediate space between compressed lumbar vertebrae.
            </p>
          </div>
          <div class="editorial-box-white" style="margin-bottom:0;">
            <div class="section-kicker">SECOND 20 TO 30 &bull; 5 CALF &amp; LYMPHATIC PUMPS</div>
            <p style="font-size: 8.4pt; color: var(--ink-soft);">
              Stand tall at the wall and perform 5 slow heel lifts to pump stagnant blood and lymphatic fluid out of your ankles and knees.
            </p>
          </div>
        </div>
      </div>

      <div class="editorial-box" style="margin-top: 8px;">
        <div class="section-kicker">WHEN TO USE THIS 30-SECOND PROTOCOL</div>
        <div class="cues-grid" style="margin-bottom:0; margin-top:4px;">
          <div class="cue-box cue-good">
            <div class="cue-title"><span>1. AFTER LONG CAR DRIVES</span></div>
            <p>Do this right next to your car door at the rest stop or garage before carrying groceries inside.</p>
          </div>
          <div class="cue-box cue-good">
            <div class="cue-title"><span>2. EVERY 90 MIN OF DESK WORK</span></div>
            <p>Walk to your office hallway wall for 30 seconds before refilling your water glass.</p>
          </div>
        </div>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Bonus Protocol #1</span>
      <span class="page-num-badge">Page 26 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 27: BONUS #2 — NIGHTTIME BED PREP WALL ROUTINE       -->
  <!-- ========================================================= -->
  <section class="page" id="page-bonus-2">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Bonus Protocol #2</span>
    </header>

    <div>
      <div class="section-kicker">PARASYMPATHETIC EVENING UNWINDING</div>
      <h2 class="serif" style="font-size: 19pt; color: var(--ink); margin-bottom: 4px;">The 3-Minute Nighttime Bed Prep Wall Routine</h2>
      <p style="font-size: 8.8pt; color: var(--ink-soft); margin-bottom: 10px;">
        If you toss and turn with aching outer hips, restless legs, or lower back spasms at 3:00 AM, it is because your body went into bed still holding daytime gravity tension. Perform this 3-minute bedroom wall sequence right before slipping under the covers.
      </p>

      <div class="day-top-grid">
        <div class="diagram-card">
          <div class="section-kicker">PARASYMPATHETIC SLEEP SWITCH</div>
          {get_posture_svg("vagal_flow", "DEEP SLEEP VAGAL CALM")}
        </div>
        <div class="why-column">
          <div class="editorial-box-white" style="margin-bottom:0;">
            <div class="section-kicker">MINUTE 1 &bull; BEDROOM WALL SACRAL MELT</div>
            <p style="font-size: 8.4pt; color: var(--ink-soft);">
              Lean your back against your bedroom wall, heels 5 inches forward. Perform 6 ultra-slow Pelvic Clock Tilts (Page 13) to flatten and release the lower back before laying horizontal on your mattress.
            </p>
          </div>
          <div class="editorial-box-white" style="margin-bottom:0;">
            <div class="section-kicker">MINUTE 2 &bull; OUTER HIP SIDE-SLEEPERS GLIDE</div>
            <p style="font-size: 8.4pt; color: var(--ink-soft);">
              Stand sideways to the wall and perform 30 seconds per side of the Outer Hip Glide (Page 15) so your hip bones don't ache when sleeping on your side.
            </p>
          </div>
          <div class="editorial-box-white" style="margin-bottom:0;">
            <div class="section-kicker">MINUTE 3 &bull; FOREHEAD REST &amp; 4–7–8 SLEEP BREATH</div>
            <p style="font-size: 8.4pt; color: var(--ink-soft);">
              Rest your forehead on your stacked hands at the wall. Inhale 4s, hold 4s, exhale 8s for 5 cycles. Your nervous system will shift directly into delta-wave readiness.
            </p>
          </div>
        </div>
      </div>

      <div class="elena-note-box" style="margin-top: 8px; padding: 10px 14px;">
        <span class="note-label">COACH ELENA'S SLEEP ALIGNMENT TIP</span>
        <p class="serif italic" style="font-size: 9pt;">
          "After doing this 3-minute wall release, if you sleep on your side, place a soft pillow between your knees and ankles. If you sleep on your back, tuck a pillow under your knees. This preserves the neutral pelvic alignment you just created at the wall all night long."
        </p>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Bonus Protocol #2</span>
      <span class="page-num-badge">Page 27 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 28: 21-DAY MASTER TRACKER (PART I: DAYS 01 TO 11)    -->
  <!-- ========================================================= -->
  <section class="page" id="page-tracker-1">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Master Log &bull; Days 01 to 11</span>
    </header>

    <div>
      <div class="section-kicker">CLINICAL CONSISTENCY &amp; SENSATION LOG</div>
      <h2 class="serif" style="font-size: 17pt; color: var(--ink); margin-bottom: 4px;">Your 21-Day Master Habit Tracker (Part I: Days 01–11)</h2>
      <p style="font-size: 8.4pt; color: var(--ink-soft); margin-bottom: 8px;">
        Print this page and keep it taped near your favorite wall space (or check off each day digitally). Rate your morning stiffness before starting (1–10) and your joint lightness afterward.
      </p>

      <table class="tracker-table">
        <thead>
          <tr>
            <th>Day</th>
            <th>Daily Wall Movement &amp; Target</th>
            <th style="text-align:center;">Pre-Stiffness</th>
            <th style="text-align:center;">Post-Ease</th>
            <th>Body Sensation / Note</th>
            <th style="text-align:center;">Done</th>
          </tr>
        </thead>
        <tbody>
          {tracker_rows_part1}
        </tbody>
      </table>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Master Habit Tracker (Part I)</span>
      <span class="page-num-badge">Page 28 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 29: 21-DAY MASTER TRACKER (PART II: DAYS 12 TO 21)   -->
  <!-- ========================================================= -->
  <section class="page" id="page-tracker-2">
    <header class="page-header">
      <div class="header-brand"><span class="brand-dot"></span><span>THE 21-DAY GENTLE WALL RESET</span></div>
      <span class="header-pill">Master Log &bull; Days 12 to 21</span>
    </header>

    <div>
      <div class="section-kicker">CLINICAL CONSISTENCY &amp; SENSATION LOG</div>
      <h2 class="serif" style="font-size: 17pt; color: var(--ink); margin-bottom: 4px;">Your 21-Day Master Habit Tracker (Part II: Days 12–21)</h2>
      <p style="font-size: 8.4pt; color: var(--ink-soft); margin-bottom: 8px;">
        Complete your final 10 days below and record your Day 21 graduation reflection at the bottom of the sheet.
      </p>

      <table class="tracker-table">
        <thead>
          <tr>
            <th>Day</th>
            <th>Daily Wall Movement &amp; Target</th>
            <th style="text-align:center;">Pre-Stiffness</th>
            <th style="text-align:center;">Post-Ease</th>
            <th>Body Sensation / Note</th>
            <th style="text-align:center;">Done</th>
          </tr>
        </thead>
        <tbody>
          {tracker_rows_part2}
        </tbody>
      </table>

      <div class="editorial-box" style="margin-top: 10px;">
        <div class="section-kicker">DAY 21 GRADUATION REFLECTION &amp; FAVORITE MOVEMENTS</div>
        <p style="font-size: 8.2pt; color: var(--ink-soft); margin-bottom: 6px;">
          Which 2 or 3 wall movements gave your body the deepest immediate relief over the past 3 weeks? Circle them as your personal non-negotiables:
        </p>
        <div class="notes-line" style="margin-bottom: 8px;"></div>
        <div class="notes-line"></div>
      </div>
    </div>

    <footer class="page-footer">
      <span>The 21-Day Gentle Wall Reset Guide &bull; Master Habit Tracker (Part II)</span>
      <span class="page-num-badge">Page 29 of 30</span>
    </footer>
  </section>

  <!-- ========================================================= -->
  <!-- PAGE 30: CERTIFICATE OF COMPLETION & CLOSING NOTE         -->
  <!-- ========================================================= -->
  <section class="page" id="page-certificate">
    <div class="cover-inner" style="justify-content: space-around;">
      <div>
        <div class="cover-edition-pill">OFFICIAL SOMATIC GRADUATION</div>
        <h2 class="serif" style="font-size: 24pt; color: var(--ink); margin-bottom: 6px;">Certificate of Completion</h2>
        <p style="font-size: 9.5pt; color: var(--ink-soft); max-width: 420px; margin: 0 auto;">
          This certifies that you have completed all 21 days of <strong>The Gentle Wall Reset Protocol</strong>, reclaiming upright spinal decompression, fluid hip mobility, and nervous system safety.
        </p>
      </div>

      <div style="width: 85%; background: #FFFFFF; border: 1pt solid var(--border-strong); border-radius: 12px; padding: 18px 22px; text-align: center;">
        <span class="mono" style="font-size: 7pt; color: var(--terracotta); letter-spacing: 0.12em;">PRESENTED WITH PRIDE TO</span>
        <div style="border-bottom: 1pt solid var(--ink); height: 28px; margin: 10px auto 14px auto; width: 80%;"></div>
        <div style="display: flex; justify-content: space-between; font-size: 8.5pt; color: var(--ink-soft); margin-top: 16px;">
          <div>
            <div style="border-bottom: 0.75pt solid var(--border-strong); width: 140px; margin-bottom: 4px; font-family: 'Fraunces', serif; font-style: italic; color: var(--sage); font-size: 11pt;">Elena Vance</div>
            <span class="mono" style="font-size: 6.5pt;">COACH ELENA VANCE</span>
          </div>
          <div>
            <div style="border-bottom: 0.75pt solid var(--border-strong); width: 140px; margin-bottom: 4px; height: 18px;"></div>
            <span class="mono" style="font-size: 6.5pt;">DATE OF COMPLETION</span>
          </div>
        </div>
      </div>

      <div class="elena-note-box" style="width: 90%; text-align: left; padding: 12px 16px;">
        <span class="note-label">A CLOSING MESSAGE FROM COACH ELENA</span>
        <p class="serif italic" style="font-size: 9.2pt; line-height: 1.48;">
          "Keep listening to your body's whispers so you never have to hear it scream. Whenever life feels heavy or your joints feel tight after travel or stress, return to your wall for 5 quiet minutes. Share your 21-day story with me anytime on Instagram at <strong>@coach.elena.vance</strong>—I read every single message."
        </p>
      </div>

      <div class="mono" style="font-size: 6.8pt; color: var(--ink-soft); width: 100%; border-top: 0.75pt solid var(--border-strong); padding-top: 8px; display: flex; justify-content: space-between;">
        <span>&copy; 2026 COACH ELENA VANCE STUDIO</span>
        <span>EDUCATIONAL WELLNESS PROTOCOL</span>
        <span>PAGE 30 OF 30</span>
      </div>
    </div>
  </section>

  <script>
    function toggleGuideDay(dayNum, checked) {{
      try {{
        if (checked) {{
          localStorage.setItem('elena_guide_day_' + dayNum, '1');
        }} else {{
          localStorage.removeItem('elena_guide_day_' + dayNum);
        }}
      }} catch (e) {{}}
    }}
    window.addEventListener('DOMContentLoaded', () => {{
      document.querySelectorAll('.day-check-input').forEach(el => {{
        const d = el.getAttribute('data-day');
        if (localStorage.getItem('elena_guide_day_' + d) === '1') {{
          el.checked = true;
        }}
      }});
    }});
  </script>
</body>
</html>
"""

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML saved to {html_out_path} ({len(html_content)} bytes)")

# Also update guia_21_dias_completa.md with the full 21-day breakdown
md_out_path = os.path.join(base_dir, "guia_21_dias_completa.md")
md_lines = [
    "# THE 21-DAY GENTLE WALL RESET GUIDE — EDICIÓN MAESTRA DE 30 PÁGINAS",
    "> **Autora:** Coach Elena Vance  ",
    "> **Formato:** Publicación Editorial A4 de 30 Páginas (HTML Interactivo + PDF de Alta Resolución)  ",
    "> **Estructura:** 4 Páginas Preliminares + 21 Páginas Diarias (1 por Día) + 2 Bonos + 2 Páginas de Tracker + Certificado  ",
    "",
    "---",
    "",
]
for d in DAYS_DATA:
    md_lines.append(f"## Día {d['day']:02d} ({d['week_title']}): {d['title']}")
    md_lines.append(f"* **Subtítulo:** {d['subtitle']}")
    md_lines.append(f"* **Dosificación:** {d['duration']} ({d['sets']}) | **Objetivo:** {d['target']}")
    md_lines.append(f"* **Por qué funciona:** {d['somatic_why']}")
    md_lines.append(f"* **Posición inicial:** {d['setup']}")
    md_lines.append("* **Pasos:**")
    for s in d["movement"]:
        md_lines.append(f"  1. {s}")
    md_lines.append(f"* **Respiración:** {d['breath']}")
    md_lines.append(f"* **Nota de Elena:** *\"{d['elena_note']}\"*")
    md_lines.append("")

with open(md_out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Markdown saved to {md_out_path}")

# Run msedge to generate the 30-page PDF
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
edge_path = next((p for p in edge_paths if os.path.exists(p)), edge_paths[0])

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={pdf_out_path}",
    html_out_path,
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge returncode:", res.returncode)
if os.path.exists(pdf_out_path):
    print(f"SUCCESS: 30-page PDF created at {pdf_out_path} (Size: {os.path.getsize(pdf_out_path)} bytes)")
else:
    print("FAILED: PDF not created")
    print("Stderr:", res.stderr)
