#!/usr/bin/env python3

"""
Parallelized script to merge mp3 and png files into mp4 files using mpi4py and ffmpeg.

This script uses the mpi4py library to distribute the work of processing mp3 and png files across 
multiple processes, enabling parallelization for faster execution. Each process takes a chunk of 
mp3 and png files, retrieves the duration of the audio files, and merges them into mp4 files using 
ffmpeg. The resulting mp4 files are saved in the specified output directory.

Usage:
    mpirun -np <num_processes> python3 mpi_mp4_merge.py /mp3/src/dir /png/src/dir /output/dir
    
    Note: It is recommended to not use more than 60% of your device's available CPU cores when
        running this script on a personal device. If running on a dedicated server, up to 
        80%-90% may be used.

Arguments:
    /mp3/src/dir: Directory containing the mp3 files. 
        Filenames must follow the format: /path/to/file/key.mp3
    /png/src/dir: Directory containing the png files, each corresponding to an mp3 file. 
        Filenames must follow the format: /path/to/file/key.png
    /output/dir: Directory where the resulting mp4 files will be saved.

    Note: All input mp3 and png files must be named with a common key, where the mp3 file is named 
        key.mp3 and the png file is named key.png. The 'key' part must match between the 
        corresponding mp3 and png files.

Parallelization:
    The script uses MPI (Message Passing Interface) to distribute the work of processing files 
    among multiple processes. The number of processes is specified with the -np flag when 
    running the script.

Performance:
    This script has been tested for performance and has shown a significant speedup in comparison 
    to the non-parallelized version, processing files 3.25 times faster with parallelization.

Dependencies:
    - mpi4py
    - ffmpeg
    - json
    - subprocess
    - os
    - sys

"""


from mpi4py import MPI
import json
import sys
import os
import subprocess
import time

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
            '-c:v', 'h264_videotoolbox', # On Mac, can use hardware 'h264_videotoolbox', otherwise 'libx264' or 'mpeg'.
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
    # Store start time for calculating script runtime
    start_time = time.time()
    
    # MPI setup
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Read files and create lists of mp3s and pngs
    if rank == 0:
        if len(sys.argv) < 4:
            print(f"Only {len(sys.argv)} input arguments.\nargv: {sys.argv}")
            print('Usage: mpirun -np <num_processes> python3 mpi_mp4_merge.py /mp3/src/dir /png/src/dir /output/dir')
            print(f"Number of CPU cores: {os.cpu_count()}\nIt is not recommended to use more than 60% of available cores.")

            return

        mp3_src_dir, png_src_dir, dest_dir = sys.argv[-3:]
        
        print(f"mp3 source directory: {mp3_src_dir}")
        print(f"png source directory: {png_src_dir}")
        print(f"Destination directory: {dest_dir}")
        
        # Create output destination if it does exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f'Destination directory not found. Created destination directory: {dest_dir}')

        # Dictionary of mp3 file paths.
        # Assumes 4-character key at the beginning of the filename which doesn't hold true for 100% of inputs.
        mp3s = {}
        for dirname, _, filenames in os.walk(mp3_src_dir):
            for filename in filenames:
                if filename.endswith(".mp3"):
                    key = os.path.splitext(filename.split("/")[-1])[0][:4]
                    mp3s[key] = os.path.join(dirname, filename)

        # Dictionary of png file paths. Keys are a string
        pngs = {}
        for dirname, _, filenames in os.walk(png_src_dir):
            for filename in filenames:
                if filename.endswith(".png"):
                    key = filename.split("/")[-1].removesuffix(".png")
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
    
    # Calculate total runtime of script
    if rank == 0:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nScript execution completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
