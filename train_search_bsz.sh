


#!/bin/bash

p_values=("lammps_48_normal"  lammps_48_abnormal)
d_values=("100ms_closed")
n_values=(48)
g_values=(1)

s_values=(60 90)
l_values=(0.5e-3 2e-3 5e-3)
b_values=(64 128)
hd_values=(16 32)

for b in "${b_values[@]}"; do
  for p in "${p_values[@]}"; do
    for d in "${d_values[@]}"; do
      for n in "${n_values[@]}"; do
        for g in "${g_values[@]}"; do
          python train.py -p "$p" -d "$d" -n "$n" -g "$g" -b "$b"
        done
      done
    done
  done
done

for h in "${hd_values[@]}"; do
  for p in "${p_values[@]}"; do
    for d in "${d_values[@]}"; do
      for n in "${n_values[@]}"; do
        for g in "${g_values[@]}"; do
          python train.py -p "$p" -d "$d" -n "$n" -g "$g" -hd "$h"
        done
      done
    done
  done
done

# python train.py -p lammps_48_normal -d 100ms_closed -n 48 -g 0 -s 30 -l 1e-3 -b 32 -hd 8
