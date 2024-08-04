# mpirun -np 16 jsirun -o /home/sx/MPI_profile/sp.B.x_16/trace --pmu --backtrace -samp_mode 1 -- /home/sx/NPB3.4.2/NPB3.4-MPI/bin/sp.B.x

# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/1ms/graph -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 2500000 -u 2500000 
# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/1ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 2500000 -u 2500000 -e

# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/10ms/graph -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 25000000 -u 25000000 
# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/10ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 25000000 -u 25000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/100ms/graph -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 250000000 -u 250000000 
# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/100ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 250000000 -u 250000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/1ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 2500000 -u 2500000 
# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/1ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 2500000 -u 2500000 -e

# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/10ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 25000000 -u 25000000 
# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/10ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 25000000 -u 25000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/100ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 250000000 -u 250000000 
# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/100ms/graph_edge -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 250000000 -u 250000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/lu.B.x/trace/ -f -o /home/sx/MPI_profile/lu.B.x/250000000/graph -d /home/sx/MPI_profile/lu.B.x/lineinfo/ -l 250000000 -u 250000000 
# timeslice_analysis -i /home/sx/MPI_profile/lu.B.x/trace/ -f -o /home/sx/MPI_profile/lu.B.x/250000000/graph_edge -d /home/sx/MPI_profile/lu.B.x/lineinfo/ -l 250000000 -u 250000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/4ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 10000000 -u 10000000
# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/4ms/graph_edge -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 10000000 -u 10000000 -e


# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/4ms/graph -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 10000000 -u 10000000
# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/4ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 10000000 -u 10000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/40ms/graph -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 100000000 -u 100000000
# timeslice_analysis -i /home/sx/MPI_profile/bt.B.x_16/trace/ -f -o /home/sx/MPI_profile/bt.B.x_16/40ms/graph_edge -d /home/sx/MPI_profile/bt.B.x_16/lineinfo/ -l 100000000 -u 100000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/40ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 100000000 -u 100000000
# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/40ms/graph_edge -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 100000000 -u 100000000 -e

# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/80ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 200000000 -u 200000000
# timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/80ms/graph_edge -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 200000000 -u 200000000 -e

timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/8ms/graph -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 20000000 -u 20000000
timeslice_analysis -i /home/sx/MPI_profile/sp.B.x_16/trace/ -f -o /home/sx/MPI_profile/sp.B.x_16/8ms/graph_edge -d /home/sx/MPI_profile/sp.B.x_16/lineinfo/ -l 20000000 -u 20000000 -e

timeslice_analysis -i /home/sx/MPI_profile/sp.C.16/trace/ -f -o /home/sx/MPI_profile/sp.C.16/100ms/graph -d /home/sx/MPI_profile/sp.C.16/lineinfo/ -l 250000000 -u 250000000
timeslice_analysis -i /home/sx/MPI_profile/sp.C.16/trace/ -f -o /home/sx/MPI_profile/sp.C.16/100ms/graph_edge -d /home/sx/MPI_profile/sp.C.16/lineinfo/ -l 250000000 -u 250000000 -e

timeslice_analysis -i /home/sx/MPI_profile/lu.C.16/trace/ -f -o /home/sx/MPI_profile/lu.C.16_closed/100ms/graph -d /home/sx/MPI_profile/lu.C.16/lineinfo/ -l 250000000 -u 250000000
timeslice_analysis -i /home/sx/MPI_profile/lu.C.16/trace/ -f -o /home/sx/MPI_profile/lu.C.16_closed/100ms/graph_edge -d /home/sx/MPI_profile/lu.C.16/lineinfo/ -l 250000000 -u 250000000 -e

timeslice_analysis -i /home/sx/MPI_profile/lu.C.16_inject_cpuocp/trace/ -f -o /home/sx/MPI_profile/lu.C.16_inject_cpuocp/100ms/graph -d /home/sx/MPI_profile/lu.C.16/lineinfo/ -l 250000000 -u 250000000
timeslice_analysis -i /home/sx/MPI_profile/lu.C.16_inject_cpuocp/trace/ -f -o /home/sx/MPI_profile/lu.C.16_inject_cpuocp/100ms/graph_edge -d /home/sx/MPI_profile/lu.C.16/lineinfo/ -l 250000000 -u 250000000 -e

timeslice_analysis -i /home/sx/MPI_profile/lulesh_27_ori/trace/ -f -o /home/sx/MPI_profile/lulesh_27_ori/100ms/graph -d /home/sx/MPI_profile/lulesh_27/lineinfo/ -l 250000000 -u 250000000
timeslice_analysis -i /home/sx/MPI_profile/lulesh_27_ori/trace/ -f -o /home/sx/MPI_profile/lulesh_27_ori/100ms/graph_edge -d /home/sx/MPI_profile/lulesh_27/lineinfo/ -l 250000000 -u 250000000 -e


timeslice_analysis -i /home/sx/MPI_profile/lu.C.16/trace/ -f -o /home/sx/MPI_profile/lu.C.16/200ms/graph -d /home/sx/MPI_profile/lu.C.16/lineinfo/ -l 500000000 -u 500000000
timeslice_analysis -i /home/sx/MPI_profile/lu.C.16/trace/ -f -o /home/sx/MPI_profile/lu.C.16/200ms/graph_edge -d /home/sx/MPI_profile/lu.C.16/lineinfo/ -l 500000000 -u 500000000 -e

timeslice_analysis -i /home/sx/MPI_profile/lammps_27_2500_nobalance/trace -f -o /home/sx/MPI_profile/lammps_27_2500_nobalance/40ms/graph -d /home/sx/MPI_profile/lammps_27_10/lineinfo -l 100000000 -u 100000000
timeslice_analysis -i /home/sx/MPI_profile/lammps_27_2500_nobalance/trace -f -o /home/sx/MPI_profile/lammps_27_2500_nobalance/40ms/graph_edge -d /home/sx/MPI_profile/lammps_27_10/lineinfo -l 100000000 -u 100000000 -e


timeslice_analysis -i /home/sx/MPI_profile/lulesh_27/trace -f -o /home/sx/MPI_profile/lulesh_27/1000ms/graph -d /home/sx/MPI_profile/lulesh_27/lineinfo -l 2500000000 -u 2500000000
timeslice_analysis -i /home/sx/MPI_profile/lulesh_27/trace -f -o /home/sx/MPI_profile/lulesh_27/1000ms/graph_edge -d /home/sx/MPI_profile/lulesh_27/lineinfo -l 2500000000 -u 2500000000 -e


dwarf_line_info_dump -i /home/sx/lammps/build/lmp -o /home/sx/MPI_profile/lammps_27_10/lineinfo
mpirun -np 27 jsirun --backtrace -samp_mode 1 -o /home/sx/MPI_profile/lammps_27_2500/trace -- lmp -in /home/sx/HPC-app/bin/in.balance.clock.static

mpirun -np 16 jsirun -o /home/sx/MPI_profile/test/trace --pmu --backtrace -samp_mode 1 -- /home/sx/NPB3.4.2/NPB3.4-MPI/bin/lu.C.x

mpirun -np 16 /home/sx/NPB3.4.2/NPB3.4-MPI/bin/lu.C.x