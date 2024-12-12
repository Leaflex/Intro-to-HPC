# ComS424
Git repository for Iowa State University's ComS 424 course, Introduction to High Performance Computing.

# Organization
- The `project/` directory contains my final project, a parallelized python script, the original non-parallelized script, and screenshots of usage, output, & performance for both.
- The `python_code/` directory contains all Python code used for the first few weeks of lab assignments.
- The `c_code/` directory contains all C code, makefiles, and screenshots of outputs from my weekly lab assignments. Note, this does not include compiled .o files. 
- The `input_files/` directory contains files used as inputs to various Python and C scripts that were run throughout the course of the class.
- The `submissions/` directory contains zip files with the source code and outputs for each lab assignment.

# Final Project - MP4 Merge Script
This project involved the development of a parallelized Python script using the Message Passing Interface (MPI, mpi4py) to merge large datasets of MP3 audio files and PNG image files into MP4 video files using the command line tool ffmpeg. The project was completed individually as part of an Intro to High-Performance Computing course at Iowa State University, but was also an improvement of a sequential version of this script I worked on for my internship at FiveQ. The script leveraged parallel processing to significantly reduce processing time by at least 3.25x for small - medium datasets compared to the sequential implementation of the same script that I had developed previously at FiveQ. The goal was to efficiently handle computationally intensive workloads by distributing tasks across multiple processes while maintaining data integrity and output quality.

The parallelized and sequential versions of the script (`mpi_mp4_merge.py` & `mp4_merge.py` respectively) along with a few screenshots of their output and performance for a small dataset can be found in the `project/` directory. The parallelized script was used to process multiple batches of mp4s after the initial testing on small datasets proved it was faster, and the result of those tests was a average speedup of about 6x for datasets of about 50 mp4s.

# HPC Cluster
- Connect with: `ssh <account>@nova.its.iastate.edu`
- SCP from cluster to local: `scp <account>@nova.its.iastate.edu:/path/to/remote/file.txt /local/path/to/save/` (run locally)
- SCP from local to cluster: `scp /path/to/file/or/directory <account>@nova.its.iastate.edu:/path/to/destination/` (destination usually `/home/<account>`)
