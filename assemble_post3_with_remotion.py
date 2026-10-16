import subprocess
import os
import sys

post3_dir = r"C:\Users\Jakes\Downloads\Ecom\03_REELS_Y_VIDEOS\POST3"

cmd = [
    'ffmpeg', '-y',
    '-i', 'clips/Woman_speaking_about_joint_pain_20261005163136.mp4',
    '-i', 'clips/Woman_explaining_with_gestures_20261005163135.mp4',
    '-i', 'clips/Woman_resting_hand_on_wall_20261005163135.mp4',
    '-i', 'clips/Elena_performs_knee_circles_20261005163135.mp4',
    '-i', 'clips/Woman_smiling_and_pointing_downward_20261005163136.mp4',
    '-i', 'musica_fondo.mp3',
    '-framerate', '30',
    '-i', 'remotion_hook_frames/element-%03d.png',
    '-filter_complex',
    '[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a]concat=n=5:v=1:a=1[vraw][araw];'
    '[vraw]scale=1080:1920:flags=lanczos,fps=30[vscaled];'
    '[vscaled][6:v]overlay=0:0:enable=\'between(t,0,3.5)\'[vhook];'
    '[vhook]ass=subtitulos_post3_dynamic.ass[vfinal];'
    '[5:a]volume=0.05,aloop=loop=-1:size=2e+09,aformat=sample_rates=48000:channel_layouts=stereo[bgm];'
    '[araw][bgm]amix=inputs=2:duration=first:dropout_transition=2[afinal]',
    '-map', '[vfinal]',
    '-map', '[afinal]',
    '-c:v', 'libx264',
    '-preset', 'slow',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    '-c:a', 'aac',
    '-b:a', '192k',
    'POST3.mp4'
]

print("Starting FFmpeg assembly with Remotion Motion Graphics Hook...")
res = subprocess.run(cmd, cwd=post3_dir, capture_output=True, text=True)

if res.returncode == 0:
    size = os.path.getsize(os.path.join(post3_dir, 'POST3.mp4'))
    print(f"SUCCESS: POST3.mp4 rendered with Remotion Hook! Size: {size / (1024*1024):.2f} MB")
else:
    print("ERROR in FFmpeg execution:")
    print(res.stderr[-1000:])
    sys.exit(1)
