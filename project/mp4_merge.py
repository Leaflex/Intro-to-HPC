#!/usr/bin/env python3
# Usage: mp4_merge.py <SERMON_SRC_DIR> <IMG_SRC_DIR> <DEST_DIR>
# Ensure ffmpeg is installed on your computer
# On Linux, switch the codec from h264_videotoolbox to libx264
# Ensure the sermon filename is of form XY12_example_series.mp3

"""Script to merge mp3 and png/PSD files into mp4 files."""

import json
import sys
import os
import subprocess

def get_duration(audio_file):
    """Returns duration of mp3 file on local file system in seconds"""
    print("IN get_duration()")
    print(f'----------audio_file----------: {audio_file}')
    get_duration_cmd = [
        'ffprobe', 
        '-v', 'error', 
        '-show_entries', 'format=duration', 
        '-of', 'json', 
        audio_file
    ]
    process = subprocess.run(get_duration_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout
    error_output = process.stderr

    # Print outputs for debugging
    print("FFprobe output:", output)
    print("FFprobe error output:", error_output)

    try:
        duration_json = json.loads(output)
        return duration_json['format']['duration']
    except (KeyError, ValueError) as e:
        raise ValueError("Could not extract duration from ffprobe output") from e

def main():
    """Merge files in SERMON_SRC_DIR and IMG_SRC_DIR files into mp4
    files at DEST_DIR
    """

    # Arguments must be directories, not files
    if len(sys.argv) < 4:
        print ('Usage: mp4_merge.py <SERMON_SRC_DIR> <IMG_SRC_DIR> <DEST_DIR>')
        return

    sermon_src_dir, img_src_dir, dest_dir = sys.argv[-3:]

    print(f"Sermon source directory: {sermon_src_dir}")
    print(f"Image source directory: {img_src_dir}")
    print(f"Destination directory: {dest_dir}")

    #create output destination if it does exist
    if not os.path.exists(dest_dir) or not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
        print(f'Destination directory not found. Created destination directory: {dest_dir}')

    # Dictionary of sermon filepaths. Keys are sermon catalog numbers
    # Input filenames must have '_' following catalog number as follows:
    # ~/path/to/file/XY12_example_series.mp3
    sermons = {}
    for dirname, dirnames, filenames in os.walk(sermon_src_dir):
        for filename in filenames:
            key = filename.split('/')[-1].split('_')[0]
            sermons[key] = os.path.join(dirname, filename)

    # Dictionary of imagefile paths. Keys are sermon catalog numbers
    # Input filenames must only be catalog numbers as follows:
    # ~/path/to/file/XY12.png
    imgs = {}
    for dirname, dirnames, filenames in os.walk(img_src_dir):
        for filename in filenames:
            key = filename.split('/')[-1].strip('.png')
            imgs[key] = os.path.join(dirname, filename)

    print(f'\n----sermons----: {sermons}\n')
    print(f'\n----imgs----: {imgs}\n')

    # For each sermon, run ffmpeg command for that sermon and its corresponding image
    keys = list(sermons.keys())
    # print number of keys
    print(f'Number of sermons: {len(keys)}')

    # Run ffmpeg command for each sermon and its corresponding image and save to destination directory.
    # Note: The filenames must follow the format XY12_example_series.mp3 for the mp3 input and XY12.png for the png input.
    # If the filenames do not follow this format, ffmpeg will throw an error.
    for catalog_num in (keys):
        print(f'Processing sermon {catalog_num}')
        output_filename = sermons[catalog_num].split('/')[-1].split('.')[0] + '.mp4'
        print(f'Output filename: {output_filename}')

        output_dest = os.path.join(dest_dir, output_filename)
        print(f'Output destination: {output_dest}\n')


        # Get duration of input file for cmd's -t option
        duration = get_duration(sermons[catalog_num])

        # ffmpeg cli input for subprocess.run
        cmd = [
            'ffmpeg',
            '-r', '1',  # Set the input frame rate to 1 fps
            '-loop', '1',  # Display the same image for the duration of the mp3 (png input tag must be next)
            '-i', imgs[catalog_num],  # png input (must follow -loop tag). See note on filename format above
            '-i', sermons[catalog_num],  # mp3 input. See note on filename format above
            '-c:v', 'h264_videotoolbox',  # Set video codec to H.264y. Alternatively can use libx264 for non mac.
            '-vf', 'scale=1920:1080',  # Set video resolution to 1920x1080
            '-pix_fmt', 'yuv420p',  # Set output pixel format to YUV 4:2:0 planar (most commonly compatible)
            '-color_range', 'pc', # Sets color range to full for yuv420 pixel format.
            '-c:a', 'aac',  # Set audio codec to AAC
            '-b:a', '192k',  # Set audio bitrate to 192k (standard for AAC)
            '-t', duration,  # Stops output file at the specified duration (same duration as input file)
            '-af', 'volume=-6dB,acompressor=threshold=0.5:ratio=2:attack=200:release=1000',  # Set audio limiter to -6dB with moderate compression
            output_dest  # Output destination
        ]

        print(f'-----------Sermon {catalog_num}-----------\n{cmd}\n\n')
        try:
            subprocess.run(cmd)
            print(f'Created {output_dest}')
        except subprocess.CalledProcessError as e:
            print(f'\n-----------------\nAn error occurred\n-----------------\n{e}')

if __name__ == "__main__":
    main()
