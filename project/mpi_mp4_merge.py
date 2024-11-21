#!/usr/bin/env python3

"""Parallelized script to merge mp3 and png files into mp4 files using mpi4py and ffmpeg."""

from mpi4py import MPI
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

def process_files(file_chunk, dest_dir, pngs, mp3s):
    """Process a chunk of files with ffmpeg"""
    for file in file_chunk:
        print(f'Processing mp3: {file}')
        output_filename = f"{file}.mp4"
        print(f'Output filename: {output_filename}')
        output_dest = os.path.join(dest_dir, output_filename)
        duration = get_duration(mp3s[file])

        cmd = [
            'ffmpeg',
            '-r', '1',
            '-loop', '1',
            '-i', pngs[file],
            '-i', mp3s[file],
            '-c:v', 'mpeg4',
            '-vf', 'scale=1920:1080',
            '-pix_fmt', 'yuv420p',
            '-color_range', 'pc',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-t', duration,
            '-af', 'volume=-6dB,acompressor=threshold=0.5:ratio=2:attack=200:release=1000',
            output_dest
        ]
        
        print(f'-----------mp3 {file}-----------\n{cmd}\n\n')

        try:
            subprocess.run(cmd, check=True)
            print(f'Created {output_dest}')
        except subprocess.CalledProcessError as e:
            print(f'\n-----------------\nAn error occurred\n-----------------\n{e}')


def main():
    """Main function for parallelized file processing"""
    # MPI setup
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Read files and create lists of mp3s and pngs
    if rank == 0:
        if len(sys.argv) < 4:
            print('Usage: mpirun -n <num_processes> python mpi_mp4_merge.py /mp3/src/dir /png/src/dir /output/dir')
            return

        mp3_src_dir, png_src_dir, dest_dir = sys.argv[-3:]
        
        print(f"mp3 source directory: {mp3_src_dir}")
        print(f"png source directory: {png_src_dir}")
        print(f"Destination directory: {dest_dir}")
        
        # Create output destination if it does exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f'Destination directory not found. Created destination directory: {dest_dir}')

        # Dictionary of mp3 filepaths.
        # ~/path/to/file/XY12.mp3
        mp3s = {}
        for dirname, _, filenames in os.walk(mp3_src_dir):
            for filename in filenames:
                key = filename.split('/')[-1].strip('.mp3')
                mp3s[key] = os.path.join(dirname, filename)
                
        # Dictionary of png filepaths.
        # Input filenames must be as follows and correspond to a mp3 key:
        # ~/path/to/file/XY12.png
        pngs = {}
        for dirname, _, filenames in os.walk(png_src_dir):
            for filename in filenames:
                key = filename.split('/')[-1].strip('.png')
                pngs[key] = os.path.join(dirname, filename)
                
        print(f'\n----mp3s----: {mp3s}\n')
        print(f'\n----pngs----: {pngs}\n')

        keys = list(mp3s.keys())
        num_files = len(keys)
        print(f'Number of mp3s: {len(keys)}')

        # Calculate chunk sizes for each process
        chunk_sizes = [(num_files // size) + (1 if i < (num_files % size) else 0) for i in range(size)]
        offsets = [sum(chunk_sizes[:i]) for i in range(size)]
        chunks = [keys[offsets[i]: offsets[i] + chunk_sizes[i]] for i in range(size)]

    else:
        # Set all parameters to none to standarize all the processes at the start
        mp3s = None
        pngs = None
        dest_dir = None
        chunks = None

    # Broadcast and scatter as blocking because processes have nothing to do until they have this information
    # Broadcast shared data (mp3s, pngs, dest_dir)
    mp3s = comm.bcast(mp3s, root=0)
    pngs = comm.bcast(pngs, root=0)
    dest_dir = comm.bcast(dest_dir, root=0)

    # Scatter chunks of keys to all processes
    local_keys = comm.scatter(chunks, root=0)

    # Each rank processes its chunk of data (including root because it's not doing anything else)
    process_files(local_keys, dest_dir, pngs, mp3s)

    # Ensure all processes finish before exiting
    comm.Barrier()

if __name__ == "__main__":
    main()
