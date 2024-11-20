#!/usr/bin/env python3

from mpi4py import MPI
import json
import sys
import os
import subprocess

def get_duration(audio_file):
    """Returns duration of mp3 file on local file system in seconds"""
    get_duration_cmd = [
        'ffprobe', 
        '-v', 'error', 
        '-show_entries', 'format=duration', 
        '-of', 'json', 
        audio_file
    ]
    process = subprocess.run(get_duration_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout

    try:
        duration_json = json.loads(output)
        return duration_json['format']['duration']
    except (KeyError, ValueError) as e:
        raise ValueError("Could not extract duration from ffprobe output") from e

def process_files(file_chunk, dest_dir, imgs, sermons):
    """Process a chunk of files with ffmpeg"""
    for catalog_num in file_chunk:
        output_filename = f"{catalog_num}.mp4"
        output_dest = os.path.join(dest_dir, output_filename)
        duration = get_duration(sermons[catalog_num])

        cmd = [
            'ffmpeg',
            '-r', '1',
            '-loop', '1',
            '-i', imgs[catalog_num],
            '-i', sermons[catalog_num],
            '-c:v', 'h264_videotoolbox',
            '-vf', 'scale=1920:1080',
            '-pix_fmt', 'yuv420p',
            '-color_range', 'pc',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-t', duration,
            '-af', 'volume=-6dB,acompressor=threshold=0.5:ratio=2:attack=200:release=1000',
            output_dest
        ]

        subprocess.run(cmd, check=True)
        print(f'Created {output_dest}')

def main():
    """Main function for parallelized file processing"""
    # MPI setup
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Read files and create lists of sermons and images
    if rank == 0:
        if len(sys.argv) < 4:
            print('Usage: mp4_merge.py <SERMON_SRC_DIR> <IMG_SRC_DIR> <DEST_DIR>')
            return

        sermon_src_dir, img_src_dir, dest_dir = sys.argv[-3:]
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        sermons = {}
        imgs = {}
        for dirname, _, filenames in os.walk(sermon_src_dir):
            for filename in filenames:
                key = filename.split('/')[-1].strip('.mp3')
                sermons[key] = os.path.join(dirname, filename)
        for dirname, _, filenames in os.walk(img_src_dir):
            for filename in filenames:
                key = filename.split('/')[-1].strip('.png')
                imgs[key] = os.path.join(dirname, filename)

        keys = list(sermons.keys())
        num_files = len(keys)

        # Calculate chunk sizes for each process
        chunk_sizes = [(num_files // size) + 
                       (1 if i < (num_files % size) else 0) for i in range(size)]
        offsets = [sum(chunk_sizes[:i]) for i in range(size)]
        chunks = [keys[offsets[i]: offsets[i] + chunk_sizes[i]] for i in range(size)]

    else:
        # Set all parameters to none to standarize all the processes at the start
        sermons = None
        imgs = None
        dest_dir = None
        chunks = None

    # Broadcast and scatter as blocking because processes
    #   have nothing to do until they have this information
    # Broadcast shared data (sermons, imgs, dest_dir)
    sermons = comm.bcast(sermons, root=0)
    imgs = comm.bcast(imgs, root=0)
    dest_dir = comm.bcast(dest_dir, root=0)

    # Scatter chunks of keys to all processes
    local_keys = comm.scatter(chunks, root=0)

    # Each rank processes its chunk of data (including root because it's not doing anything else)
    process_files(local_keys, dest_dir, imgs, sermons)

    # Ensure all processes finish before exiting
    comm.Barrier()

if __name__ == "__main__":
    main()
