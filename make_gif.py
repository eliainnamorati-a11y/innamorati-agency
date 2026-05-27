import os
import glob

try:
    from PIL import Image
except ImportError:
    import sys
    print("Pillow not installed. Please install it.")
    sys.exit(1)

def make_gif():
    frame_folder = 'about/rolls royce video'
    frames = sorted(glob.glob(os.path.join(frame_folder, '*.jpg')))
    
    if not frames:
        print("No frames found in", frame_folder)
        return
        
    print(f"Found {len(frames)} frames.")
    imgs = [Image.open(f) for f in frames]
    
    # Create the gif
    out_path = 'rolls royce/rolls-royce-ezgif.gif'
    imgs[0].save(out_path, format='GIF', append_images=imgs[1:], save_all=True, duration=80, loop=0)
    print("Created animated GIF at", out_path)

if __name__ == '__main__':
    make_gif()
