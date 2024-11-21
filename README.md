# ComS424
Git repository for ComS 424, Introduction to High Performance Computing

# Organization
- Python files can be found in the `python_code/` directory.
- C files can be found in the `c_code/` directory. Note, this does not include compiled .o files. These have been git ignored to reduce clutter.
- Input files can be found in the `input_files/` directory. These are to be used for inputs to the Python and C scripts.
- The `submissions/` directory contains zip files with the source code and a submission of the output for each lab assignment.
- The `project/` directory contains my final project, a parallelized python script, the original non-parallelized script, and screenshots of usage, output, & performance for both.

# HPC Cluster
- Connect with: `ssh <account>@nova.its.iastate.edu`
- SCP from cluster to local: `scp <account>@nova.its.iastate.edu:/path/to/remote/file.txt /local/path/to/save/` (run locally)
- SCP from local to cluster: `scp /path/to/file/or/directory <account>@nova.its.iastate.edu:/path/to/destination/` (destination usually `/home/<account>`)
