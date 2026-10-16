"""
Comprehensive Anatomical Posture SVG Engine for Elena Vance's 21-Day Gentle Wall Reset Guide.
Generates 21 bespoke volumetric organic human silhouettes (Kinfolk x Aesop x Somatic Studio aesthetic)
with architectural wall support, internal vertebral spine axis, tactile contact points,
glowing decompression targets, and vagal breath rhythm badges.
"""

def _common_svg_frame(inner_content: str, day_label: str, breath_cue: str, target_zone: str) -> str:
    return f"""<svg viewBox="0 0 220 195" class="posture-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Card Background -->
  <rect x="2" y="2" width="216" height="191" rx="10" fill="#FAF6F0" stroke="#D9CEBE" stroke-width="1"/>
  
  <!-- Top Status Bar -->
  <text x="14" y="16" font-family="JetBrains Mono, monospace" font-size="6.2" font-weight="700" fill="#46594B" letter-spacing="0.4">{day_label.upper()}</text>
  <rect x="154" y="7" width="52" height="13" rx="3.5" fill="#F2ECE1" stroke="#D9CEBE" stroke-width="0.7"/>
  <text x="180" y="16" font-family="JetBrains Mono, monospace" font-size="5.6" font-weight="700" fill="#B87352" text-anchor="middle">{breath_cue}</text>
  
  {inner_content}
  
  <!-- Target Zone Capsule (Bottom Right) -->
  <rect x="116" y="166" width="94" height="18" rx="3.5" fill="#F2ECE1" stroke="#D9CEBE" stroke-width="0.8"/>
  <text x="163" y="178" font-family="JetBrains Mono, monospace" font-size="6.2" font-weight="700" fill="#18221B" text-anchor="middle">{target_zone[:24].upper()}</text>
</svg>"""

def _wall_left() -> str:
    return """
  <!-- Architectural Left Wall Structure -->
  <rect x="18" y="22" width="10" height="156" rx="1.5" fill="#EAE3D2" stroke="#8C7A6B" stroke-width="1"/>
  <line x1="18" y1="38" x2="28" y2="30" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="58" x2="28" y2="50" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="78" x2="28" y2="70" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="98" x2="28" y2="90" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="118" x2="28" y2="110" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="138" x2="28" y2="130" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="158" x2="28" y2="150" stroke="#8C7A6B" stroke-width="0.8"/>
  <line x1="18" y1="174" x2="28" y2="166" stroke="#8C7A6B" stroke-width="0.8"/>
  <!-- Plumb Alignment Line -->
  <line x1="28" y1="22" x2="28" y2="178" stroke="#46594B" stroke-width="1.2" stroke-dasharray="3 2.5"/>
  <!-- Floor Support Line -->
  <line x1="12" y1="178" x2="208" y2="178" stroke="#46594B" stroke-width="1.6" stroke-linecap="round"/>
  <text x="12" y="186" font-family="JetBrains Mono, monospace" font-size="5" fill="#8C7A6B">GROUND SUPPORT</text>
    """

def get_posture_svg_v2(pose_id: str, target_zone: str, day_num: int = 1) -> str:
    """Returns an ultra-detailed somatic posture SVG for the given day/pose."""
    
    # Normalize pose_id if numerical day is known
    # ==================== DAY 01: THE WALL PALMS PRESS ====================
    if day_num == 1 or pose_id in ("day_01_palms_press",):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="72" r="8" fill="#B87352" fill-opacity="0.22" stroke="#B87352" stroke-width="1.2"/>
  <circle cx="28" cy="72" r="3.2" fill="#B87352"/>
  
  <g id="figure">
    <path d="M 96 122 C 94 136, 92 152, 91 165 L 90 178 L 102 178 L 101 165 C 101 152, 102 136, 104 122 Z" fill="#DDD1BF" stroke="#18221B" stroke-width="1"/>
    <path d="M 100 120 C 97 132, 94 144, 93 150 C 92 155, 93 166, 94 178 L 107 178 C 106 166, 106 156, 105 150 C 104 144, 107 132, 110 120 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <circle cx="94" cy="150" r="3" fill="none" stroke="#46594B" stroke-width="0.9" stroke-dasharray="1.5 1.5"/>
    
    <path d="M 88 58 C 84 66, 82 78, 86 92 C 90 106, 96 114, 100 122 L 110 120 C 106 110, 100 98, 98 84 C 96 72, 97 64, 96 58 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.4"/>
    <path d="M 90 60 Q 86 86 98 116" fill="none" stroke="#B87352" stroke-width="2.2" stroke-dasharray="3 2"/>
    
    <circle cx="95" cy="104" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="95" cy="104" r="3.2" fill="#B87352"/>
    
    <path d="M 88 62 L 28 69 L 28 73 L 88 66 Z" fill="#DDD1BF" stroke="#18221B" stroke-width="0.9"/>
    <path d="M 92 60 C 80 62, 68 64, 56 67 C 46 69, 38 71, 28 72 L 28 76 C 38 75, 48 73, 58 71 C 70 68, 82 66, 94 64 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <ellipse cx="28" cy="74" rx="2" ry="4" fill="#EAE0D0" stroke="#18221B" stroke-width="1"/>
    
    <ellipse cx="98" cy="48" rx="4.5" ry="5.5" fill="#32261E"/>
    <path d="M 88 38 C 94 38, 97 42, 96 48 C 95 54, 91 56, 86 56 C 81 56, 79 52, 79 47 C 79 42, 82 38, 88 38 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 83 42 C 86 38, 92 37, 96 40 C 97 44, 97 49, 95 52 C 93 47, 88 44, 83 45 Z" fill="#32261E"/>
  </g>
  
  <line x1="28" y1="168" x2="94" y2="168" stroke="#8C7A6B" stroke-width="1" stroke-dasharray="2 2"/>
  <polygon points="28,168 33,165 33,171" fill="#8C7A6B"/>
  <polygon points="94,168 89,165 89,171" fill="#8C7A6B"/>
  <text x="61" y="164" font-family="JetBrains Mono, monospace" font-size="5.8" fill="#8C7A6B" text-anchor="middle">ARM'S LENGTH</text>
  
  <g transform="translate(126, 40)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">AXIAL TRACTION</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Gravity unloads 70%</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">of L4–L5 disc pressure</text>
  </g>
  <text x="115" y="152" font-family="JetBrains Mono, monospace" font-size="5.5" font-weight="600" fill="#46594B">SOFT KNEES 15°</text>
  <line x1="97" y1="150" x2="112" y2="150" stroke="#46594B" stroke-width="0.8" stroke-dasharray="2 1.5"/>
        """
        return _common_svg_frame(inner, f"DAY 01 · PALMS PRESS", "4s IN · 6s EX", target_zone)

    # ==================== DAY 02: SCAPULAR WALL MELT ====================
    elif day_num == 2 or pose_id in ("day_02_scapular_melt",):
        inner = f"""
  {_wall_left()}
  <rect x="25" y="48" width="6" height="40" rx="3" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2"/>
  <circle cx="28" cy="50" r="3" fill="#B87352"/>
  <circle cx="28" cy="86" r="3" fill="#B87352"/>
  <circle cx="28" cy="42" r="5" fill="#46594B" fill-opacity="0.2" stroke="#46594B" stroke-width="1"/>
  
  <g id="figure">
    <path d="M 76 122 C 75 136, 74 152, 73 165 L 72 178 L 84 178 L 84 165 C 84 152, 85 136, 86 122 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 68 56 C 60 68, 58 84, 62 98 C 66 110, 72 116, 76 122 L 86 122 C 82 114, 76 102, 74 88 C 72 74, 74 64, 76 56 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.4"/>
    <path d="M 70 56 Q 64 82 76 116" fill="none" stroke="#B87352" stroke-width="2.2" stroke-dasharray="3 2"/>
    <circle cx="65" cy="74" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="65" cy="74" r="3" fill="#B87352"/>
    <path d="M 72 58 L 28 84 L 28 50 L 32 50 L 32 80 L 74 64 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <ellipse cx="64" cy="38" rx="4" ry="5" fill="#32261E"/>
    <path d="M 48 34 C 54 34, 62 36, 62 44 C 62 50, 56 54, 48 52 C 40 50, 32 46, 30 42 C 30 38, 40 34, 48 34 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
  </g>
  
  <g transform="translate(126, 44)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">SCAPULAR GLIDE</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Shoulder blades slide</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">together &amp; release neck</text>
  </g>
  <text x="110" y="118" font-family="JetBrains Mono, monospace" font-size="5.5" font-weight="600" fill="#46594B">FOREARMS FLAT</text>
  <line x1="32" y1="70" x2="108" y2="114" stroke="#46594B" stroke-width="0.8" stroke-dasharray="2 1.5"/>
        """
        return _common_svg_frame(inner, f"DAY 02 · SCAPULAR MELT", "4s IN · 6s EX", target_zone)

    # ==================== DAY 03: STANDING L-TRACTION HINGE ====================
    elif day_num in (3, 17) or pose_id in ("day_03_l_traction", "l_traction"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="88" r="8" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2"/>
  <circle cx="28" cy="88" r="3.2" fill="#B87352"/>
  
  <g id="figure">
    <path d="M 134 94 C 130 110, 126 134, 124 148 C 122 155, 124 166, 126 178 L 138 178 C 136 166, 134 154, 136 148 C 138 134, 142 110, 146 94 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.4"/>
    <circle cx="125" cy="148" r="3.2" fill="none" stroke="#46594B" stroke-width="0.9" stroke-dasharray="1.5 1.5"/>
    <path d="M 72 82 C 90 82, 114 83, 134 85 C 138 88, 144 94, 146 102 L 134 102 C 128 97, 112 94, 94 92 C 82 92, 74 90, 72 88 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.4"/>
    <line x1="72" y1="86" x2="134" y2="86" stroke="#B87352" stroke-width="2.2" stroke-dasharray="3 2"/>
    <circle cx="126" cy="86" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="126" cy="86" r="3.5" fill="#B87352"/>
    <path d="M 72 82 L 28 86 L 28 90 L 72 88 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <ellipse cx="68" cy="74" rx="4" ry="4.5" fill="#32261E"/>
    <circle cx="62" cy="78" r="8" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
  </g>
  
  <line x1="148" y1="86" x2="182" y2="86" stroke="#B87352" stroke-width="1.6"/>
  <polygon points="186,86 178,82 178,90" fill="#B87352"/>
  <text x="165" y="78" font-family="JetBrains Mono, monospace" font-size="6.2" font-weight="700" fill="#B87352" text-anchor="middle">L4–L5 TRACTION</text>
  <text x="145" y="146" font-family="JetBrains Mono, monospace" font-size="5.5" font-weight="600" fill="#46594B">SOFT BENT KNEES</text>
  <line x1="128" y1="148" x2="142" y2="146" stroke="#46594B" stroke-width="0.8" stroke-dasharray="2 1.5"/>
        """
        label = "DAY 17 · POSTERIOR CHAIN" if day_num == 17 else "DAY 03 · L-TRACTION HINGE"
        return _common_svg_frame(inner, label, "4s IN · 6s EX", target_zone)

    # ==================== DAY 04: WALL CAT-COW WAVE ====================
    elif day_num in (4, 20) or pose_id in ("day_04_cat_cow", "spinal_wave"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="74" r="6" fill="#B87352" fill-opacity="0.22" stroke="#B87352" stroke-width="1"/>
  
  <g id="figure-wave">
    <path d="M 88 122 C 86 136, 84 152, 83 165 L 82 178 L 94 178 L 94 165 C 94 152, 95 136, 96 122 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 80 58 Q 98 88 88 120" fill="none" stroke="#46594B" stroke-width="2" stroke-dasharray="2.5 2"/>
    <path d="M 80 58 Q 66 88 88 120 L 96 120 Q 76 88 88 58 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <circle cx="75" cy="72" r="3" fill="#B87352"/>
    <circle cx="72" cy="88" r="3.5" fill="#B87352"/>
    <circle cx="76" cy="104" r="3" fill="#B87352"/>
    <path d="M 82 62 L 28 74 L 28 78 L 84 66 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
    <ellipse cx="88" cy="48" rx="4" ry="5" fill="#32261E"/>
    <circle cx="78" cy="46" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="42" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">SEGMENTAL WAVE</text>
    <text x="8" y="22" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">1. Tuck tailbone under</text>
    <text x="8" y="31" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">2. Round mid-back pearls</text>
    <text x="8" y="39" font-family="Plus Jakarta Sans, sans-serif" font-size="5.5" fill="#46594B">Zero knee floor torque</text>
  </g>
        """
        label = "DAY 20 · MASTER FLOW" if day_num == 20 else "DAY 04 · CAT-COW WAVE"
        return _common_svg_frame(inner, label, "IN: Arch · EX: Round", target_zone)

    # ==================== DAY 05: LATERAL RIBCAGE & QL ARC ====================
    elif day_num in (5, 11) or pose_id in ("day_05_lateral_ql_arc", "lateral_arc"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="78" r="6" fill="#46594B" fill-opacity="0.25" stroke="#46594B" stroke-width="1.2"/>
  
  <g id="figure-arc">
    <path d="M 88 122 L 86 178 L 98 178 L 98 122 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 82 60 C 86 78, 98 94, 94 122 L 104 122 C 108 94, 96 76, 92 60 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.4"/>
    <path d="M 86 64 Q 102 92 98 120" fill="none" stroke="#B87352" stroke-width="2.5" stroke-dasharray="3 2"/>
    <circle cx="100" cy="94" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="100" cy="94" r="3.2" fill="#B87352"/>
    <path d="M 84 68 L 28 78 L 28 82 L 84 72 Z" fill="#DDD1BF" stroke="#18221B" stroke-width="1"/>
    <path d="M 90 62 C 86 44, 76 28, 48 30 C 44 31, 38 34, 34 38 L 36 42 C 40 38, 46 35, 52 34 C 74 34, 82 48, 86 64 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <ellipse cx="94" cy="52" rx="4" ry="5" fill="#32261E"/>
    <circle cx="85" cy="48" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <path d="M 108 82 Q 116 94 112 110" fill="none" stroke="#B87352" stroke-width="1.4" stroke-dasharray="2 2"/>
  <polygon points="112,112 109,106 115,107" fill="#B87352"/>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">SIDE-BODY UNWIND</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Opens compressed QL</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">&amp; lower ribcage fascia</text>
  </g>
        """
        label = "DAY 11 · SCIATIC GLIDE" if day_num == 11 else "DAY 05 · LATERAL QL ARC"
        return _common_svg_frame(inner, label, "4s IN · 6s EX", target_zone)

    # ==================== DAY 06: THORACIC OPEN-BOOK AT WALL ====================
    elif day_num == 6:
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="70" r="5" fill="#46594B" fill-opacity="0.25" stroke="#46594B" stroke-width="1.2"/>
  
  <g id="figure-open-book">
    <path d="M 82 120 L 80 178 L 92 178 L 94 120 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 80 58 C 78 74, 80 96, 82 120 L 92 120 C 92 96, 92 74, 90 58 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <!-- Rotational Mid-Back Node -->
    <circle cx="86" cy="80" r="8" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="86" cy="80" r="3" fill="#B87352"/>
    
    <!-- Arm 1 Anchored to Wall -->
    <line x1="82" y1="68" x2="28" y2="70" stroke="#18221B" stroke-width="2.2" stroke-linecap="round"/>
    
    <!-- Arm 2 Sweeping Open Backward (180° Arch) -->
    <path d="M 86 68 Q 112 50 148 64" fill="none" stroke="#B87352" stroke-width="2.2" stroke-dasharray="3 2"/>
    <polygon points="152,66 144,61 146,69" fill="#B87352"/>
    
    <ellipse cx="90" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="82" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">THORACIC ROTATION</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Frees locked middle-back</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">&amp; opens tight chest</text>
  </g>
        """
        return _common_svg_frame(inner, f"DAY 06 · THORACIC OPEN-BOOK", "Inhale Open · Exhale Return", target_zone)

    # ==================== DAY 07: VAGAL BREATH & SPINE FLOW ====================
    elif day_num in (7, 21) or pose_id in ("day_07_vagal_flow", "vagal_flow"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="46" r="4" fill="#46594B" fill-opacity="0.3"/>
  <circle cx="28" cy="68" r="5" fill="#46594B" fill-opacity="0.3"/>
  <circle cx="28" cy="114" r="5" fill="#46594B" fill-opacity="0.3"/>
  
  <g id="figure-vagal">
    <path d="M 40 120 L 44 178 L 56 178 L 52 120 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 28 60 C 32 74, 38 88, 38 102 C 38 112, 34 118, 30 122 L 42 122 C 48 114, 52 100, 50 82 C 48 68, 44 60, 38 56 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 38 64 C 44 74, 46 84, 42 88 L 38 86" fill="none" stroke="#18221B" stroke-width="2" stroke-linecap="round"/>
    <ellipse cx="24" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="34" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <circle cx="48" cy="80" r="14" fill="none" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2.5 2"/>
  <circle cx="48" cy="80" r="26" fill="none" stroke="#46594B" stroke-width="1" stroke-dasharray="3 3"/>
  <circle cx="48" cy="80" r="38" fill="none" stroke="#8C7A6B" stroke-width="0.8" stroke-dasharray="4 4"/>
  
  <g transform="translate(124, 42)">
    <rect x="0" y="0" width="84" height="42" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#46594B">VAGUS NERVE SWITCH</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">1. Expand belly 4s (IN)</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">2. Soft sigh 6s (EX)</text>
    <text x="8" y="39" font-family="JetBrains Mono, monospace" font-size="5.2" fill="#B87352">Lowers morning cortisol</text>
  </g>
        """
        label = "DAY 21 · LIFELONG RESET" if day_num == 21 else "DAY 07 · VAGAL BREATH"
        return _common_svg_frame(inner, label, "4s IN · 6s EX", target_zone)

    # ==================== DAY 08: STANDING HIP CIRCLES ====================
    elif day_num in (8, 18) or pose_id in ("day_08_hip_circles", "hip_circles"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="74" r="6" fill="#46594B" fill-opacity="0.25" stroke="#46594B" stroke-width="1.2"/>
  
  <g id="figure-hip">
    <path d="M 86 116 L 84 178 L 96 178 L 96 116 Z" fill="#DDD1BF" stroke="#18221B" stroke-width="1.1"/>
    <path d="M 88 56 C 84 72, 84 94, 86 116 L 98 116 C 98 94, 98 72, 96 56 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <circle cx="94" cy="116" r="10" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="94" cy="116" r="3.5" fill="#B87352"/>
    
    <path d="M 94 116 C 104 122, 116 130, 120 140 C 116 150, 110 162, 108 170" fill="none" stroke="#18221B" stroke-width="2.6" stroke-linecap="round"/>
    
    <ellipse cx="122" cy="138" rx="16" ry="10" fill="none" stroke="#B87352" stroke-width="1.4" stroke-dasharray="3 2"/>
    <polygon points="138,138 135,133 141,133" fill="#B87352"/>
    
    <path d="M 88 64 L 28 74 L 28 78 L 88 68 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
    <ellipse cx="98" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="88" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">SYNOVIAL LUBRICATION</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">5 micro-circles each way</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Releases pinching nerve</text>
  </g>
        """
        label = "DAY 18 · CROSS-BODY PENDULUM" if day_num == 18 else "DAY 08 · HIP CIRCLES"
        return _common_svg_frame(inner, label, "Slow & Rhythmic", target_zone)

    # ==================== DAY 09: PELVIC CLOCK (12-TO-6 TILT) ====================
    elif day_num == 9 or pose_id in ("day_09_pelvic_tilt", "pelvic_tilt"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="112" r="7" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2"/>
  <circle cx="28" cy="112" r="3.2" fill="#B87352"/>
  
  <g id="figure-pelvic">
    <path d="M 38 116 L 46 178 L 58 178 L 50 116 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 28 58 C 34 74, 40 88, 38 104 C 36 112, 32 116, 28 118 L 40 118 C 46 112, 48 98, 48 80 C 46 66, 42 58, 36 54 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <line x1="56" y1="92" x2="32" y2="92" stroke="#B87352" stroke-width="1.8"/>
    <polygon points="29,92 35,88 35,96" fill="#B87352"/>
    
    <ellipse cx="24" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="34" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(136, 68)">
    <circle cx="26" cy="26" r="24" fill="#FAF6F0" stroke="#46594B" stroke-width="1.3"/>
    <path d="M 26 8 A 18 18 0 0 1 26 44" fill="none" stroke="#B87352" stroke-width="1.8" stroke-dasharray="2.5 2"/>
    <circle cx="26" cy="8" r="2.8" fill="#B87352"/>
    <circle cx="26" cy="44" r="2.8" fill="#46594B"/>
    <text x="26" y="2" font-family="JetBrains Mono, monospace" font-size="5.8" font-weight="700" fill="#B87352" text-anchor="middle">12:00 TUCK</text>
    <text x="26" y="52" font-family="JetBrains Mono, monospace" font-size="5.8" font-weight="700" fill="#46594B" text-anchor="middle">6:00 RELEASE</text>
  </g>
        """
        return _common_svg_frame(inner, f"DAY 09 · PELVIC CLOCK", "Tuck 12h · Release 6h", target_zone)

    # ==================== DAY 10: ZERO-KNEEL PSOAS RELEASE ====================
    elif day_num in (10, 14) or pose_id in ("day_10_psoas_release", "psoas_release"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="70" r="6" fill="#46594B" fill-opacity="0.25" stroke="#46594B" stroke-width="1.2"/>
  
  <g id="figure-psoas">
    <path d="M 84 116 C 96 130, 114 152, 126 178 L 138 178 C 126 150, 108 126, 94 116 Z" fill="#DDD1BF" stroke="#18221B" stroke-width="1.1"/>
    <path d="M 80 116 L 68 150 L 68 178 L 78 178 L 78 152 L 88 116 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <path d="M 80 56 C 76 74, 76 96, 78 116 L 90 116 C 90 96, 92 74, 90 56 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <path d="M 78 92 Q 86 114 104 136" fill="none" stroke="#B87352" stroke-width="3" stroke-linecap="round"/>
    <circle cx="86" cy="114" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="86" cy="114" r="3.5" fill="#B87352"/>
    
    <path d="M 80 64 L 28 70 L 28 74 L 80 68 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
    <ellipse cx="90" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="80" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">ZERO-KNEEL PSOAS</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Tuck tailbone slightly</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Zero knee floor contact</text>
  </g>
        """
        label = "DAY 14 · FLUIDITY FLOW" if day_num == 14 else "DAY 10 · STANDING PSOAS"
        return _common_svg_frame(inner, label, "4s IN · 6s EX", target_zone)

    # ==================== DAY 12: PATELLA OFFLOAD & ANKLE GLIDE ====================
    elif day_num in (12, 19) or pose_id in ("day_12_patella_offload", "knee_glide"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="74" r="9" fill="#46594B" fill-opacity="0.25" stroke="#46594B" stroke-width="1.3"/>
  <circle cx="28" cy="74" r="3.5" fill="#46594B"/>
  
  <g id="figure-knee">
    <path d="M 80 114 C 74 130, 68 144, 68 152 C 68 160, 74 168, 76 174 L 88 174 C 86 168, 80 160, 80 152 C 82 144, 88 130, 92 114 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <circle cx="70" cy="150" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="70" cy="150" r="3.5" fill="#B87352"/>
    <circle cx="78" cy="172" r="4.5" fill="#46594B" fill-opacity="0.25"/>
    
    <path d="M 82 56 C 80 72, 80 94, 82 114 L 92 114 C 92 94, 94 72, 92 56 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 82 64 L 28 74 L 28 78 L 82 68 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
    <ellipse cx="92" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="82" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">ZERO KNEE TORQUE</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">70% weight on wall</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Smooth synovia pump</text>
  </g>
        """
        label = "DAY 19 · LYMPHATIC FLUSH" if day_num == 19 else "DAY 12 · PATELLA OFFLOAD"
        return _common_svg_frame(inner, label, "Smooth Glide", target_zone)

    # ==================== DAY 13: SUPPORTED STANDING FIGURE-4 UNWIND ====================
    elif day_num == 13:
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="74" r="7" fill="#46594B" fill-opacity="0.25" stroke="#46594B" stroke-width="1.2"/>
  
  <g id="figure-fig4">
    <!-- Standing Base Leg (Bent knee 20° like high stool sit) -->
    <path d="M 84 116 C 80 134, 76 154, 76 178 L 88 178 C 88 156, 92 136, 94 116 Z" fill="#DDD1BF" stroke="#18221B" stroke-width="1.1"/>
    
    <!-- Crossed Foot / Figure-4 Leg -->
    <path d="M 88 116 C 104 120, 114 130, 112 138 C 106 142, 92 142, 82 140" fill="none" stroke="#18221B" stroke-width="2.6" stroke-linecap="round"/>
    
    <!-- Glowing Outer Hip & Piriformis Release -->
    <circle cx="106" cy="132" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="106" cy="132" r="3.2" fill="#B87352"/>
    
    <!-- Torso Hinged Gracefully -->
    <path d="M 82 58 C 80 76, 82 98, 86 116 L 96 116 C 96 98, 96 76, 92 58 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 84 66 L 28 74 L 28 78 L 84 70 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
    
    <ellipse cx="94" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="84" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">PIRIFORMIS UNWIND</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Standing figure-4 shape</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Unlocks pinched sciatica</text>
  </g>
        """
        return _common_svg_frame(inner, f"DAY 13 · STANDING FIGURE-4", "4s IN · 6s EX", target_zone)

    # ==================== DAY 15: SUPPORTED WALL ANGELS ====================
    elif day_num == 15 or pose_id in ("day_15_wall_angels", "wall_angels"):
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="46" r="4" fill="#46594B" fill-opacity="0.3"/>
  <circle cx="28" cy="68" r="5" fill="#46594B" fill-opacity="0.3"/>
  <circle cx="28" cy="116" r="5" fill="#46594B" fill-opacity="0.3"/>
  
  <g id="figure-profile">
    <path d="M 38 116 L 46 178 L 58 178 L 50 116 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 28 58 C 34 74, 40 88, 38 104 C 36 112, 32 116, 28 118 L 40 118 C 46 112, 48 98, 48 80 C 46 66, 42 58, 36 54 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <ellipse cx="24" cy="46" rx="4" ry="5" fill="#32261E"/>
    <circle cx="34" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <!-- Inset: Cactus 'W' to 'V' Scapular Glide Pattern -->
  <g transform="translate(114, 38)">
    <rect x="0" y="0" width="94" height="114" rx="5" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="47" y="14" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352" text-anchor="middle">W-TO-V SCAPULAR GLIDE</text>
    <circle cx="47" cy="30" r="6" fill="#EAE0D0" stroke="#18221B" stroke-width="1"/>
    <ellipse cx="47" cy="27" rx="3.5" ry="3" fill="#32261E"/>
    <line x1="47" y1="36" x2="47" y2="84" stroke="#18221B" stroke-width="1.8"/>
    <path d="M 20 46 L 30 68 L 47 68 L 64 68 L 74 46" fill="none" stroke="#18221B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    <line x1="20" y1="42" x2="20" y2="28" stroke="#B87352" stroke-width="1.4"/>
    <polygon points="20,25 17,31 23,31" fill="#B87352"/>
    <line x1="74" y1="42" x2="74" y2="28" stroke="#B87352" stroke-width="1.4"/>
    <polygon points="74,25 71,31 77,31" fill="#B87352"/>
    <circle cx="47" cy="68" r="8" fill="#B87352" fill-opacity="0.22" stroke="#B87352" stroke-width="1" stroke-dasharray="2 2"/>
    <text x="47" y="96" font-family="Plus Jakarta Sans, sans-serif" font-size="5.5" fill="#46594B" text-anchor="middle">Wrists &amp; elbows flush</text>
    <text x="47" y="104" font-family="Plus Jakarta Sans, sans-serif" font-size="5.5" fill="#46594B" text-anchor="middle">to wall plaster</text>
  </g>
        """
        return _common_svg_frame(inner, f"DAY 15 · WALL ANGELS", "4s IN (V) · 6s EX (W)", target_zone)

    # ==================== DAY 16: SUBOCCIPITAL & JAW RELEASE ====================
    elif day_num == 16:
        inner = f"""
  {_wall_left()}
  <!-- Head Flush Contact with Wall at Occiput (y=44) -->
  <circle cx="28" cy="44" r="6" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2"/>
  <circle cx="28" cy="44" r="2.8" fill="#B87352"/>
  
  <g id="figure-cervical">
    <path d="M 38 116 L 46 178 L 58 178 L 50 116 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <path d="M 28 58 C 34 74, 40 88, 38 104 C 36 112, 32 116, 28 118 L 40 118 C 46 112, 48 98, 48 80 C 46 66, 42 58, 36 54 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    
    <!-- Cervical Spine Line (C1-C7) -->
    <path d="M 30 46 C 30 52, 32 58, 36 64" fill="none" stroke="#B87352" stroke-width="2.4" stroke-dasharray="2.5 1.5"/>
    <circle cx="30" cy="48" r="8" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    
    <!-- Retrusion Vector Arrow (Gentle Double-Chin Pull) -->
    <line x1="52" y1="52" x2="38" y2="52" stroke="#46594B" stroke-width="1.6"/>
    <polygon points="35,52 41,49 41,55" fill="#46594B"/>
    
    <!-- Head Profile -->
    <ellipse cx="24" cy="44" rx="4" ry="5" fill="#32261E"/>
    <circle cx="34" cy="44" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.2"/>
  </g>
  
  <!-- Crown Lengthening Vector (Upward) -->
  <line x1="34" y1="34" x2="34" y2="22" stroke="#B87352" stroke-width="1.5"/>
  <polygon points="34,19 31,25 37,25" fill="#B87352"/>
  <text x="56" y="26" font-family="JetBrains Mono, monospace" font-size="5.5" font-weight="700" fill="#B87352">CROWN LIFT</text>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">C1–C2 DECOMPRESSION</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Gentle chin retraction</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Relieves neck &amp; jaw ache</text>
  </g>
        """
        return _common_svg_frame(inner, f"DAY 16 · SUBOCCIPITAL RESET", "4s IN · 6s EX", target_zone)

    # ==================== FALLBACK / MASTER SOMATIC ARCHETYPE ====================
    else:
        inner = f"""
  {_wall_left()}
  <circle cx="28" cy="74" r="8" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2"/>
  <circle cx="28" cy="74" r="3.2" fill="#B87352"/>
  
  <g id="figure-master">
    <path d="M 94 120 C 92 136, 90 152, 90 165 L 89 178 L 101 178 L 101 165 C 101 152, 102 136, 104 120 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <circle cx="91" cy="150" r="3" fill="none" stroke="#46594B" stroke-width="0.9" stroke-dasharray="1.5 1.5"/>
    <path d="M 88 58 C 84 66, 82 78, 86 92 C 90 106, 96 114, 100 120 L 110 118 C 106 110, 100 98, 98 84 C 96 72, 97 64, 96 58 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.4"/>
    <path d="M 90 60 Q 86 86 98 116" fill="none" stroke="#B87352" stroke-width="2.2" stroke-dasharray="3 2"/>
    <circle cx="95" cy="102" r="9" fill="#B87352" fill-opacity="0.25" stroke="#B87352" stroke-width="1.2" stroke-dasharray="2 2"/>
    <circle cx="95" cy="102" r="3.2" fill="#B87352"/>
    <path d="M 92 60 L 28 72 L 28 76 L 94 64 Z" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
    <ellipse cx="98" cy="48" rx="4.5" ry="5.5" fill="#32261E"/>
    <circle cx="88" cy="46" r="7.5" fill="#EAE0D0" stroke="#18221B" stroke-width="1.3"/>
  </g>
  
  <g transform="translate(126, 42)">
    <rect x="0" y="0" width="82" height="38" rx="4" fill="#FAF6F0" stroke="#E6DEC9" stroke-width="0.8"/>
    <text x="8" y="11" font-family="JetBrains Mono, monospace" font-size="6" font-weight="700" fill="#B87352">SOMATIC RESET</text>
    <text x="8" y="21" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">Zero floor strain</text>
    <text x="8" y="30" font-family="Plus Jakarta Sans, sans-serif" font-size="5.8" fill="#18221B">100% upright wall stability</text>
  </g>
        """
        return _common_svg_frame(inner, f"DAY {day_num:02d} · SOMATIC RESET", "4s IN · 6s EX", target_zone)
