#!/bin/bash

usage() {
    echo "Usage: $0 -i INPUT -d DURATION -u INTERVAL"
    exit 1
}

# 解析命令行参数
while getopts "i:d:u:" opt; do
    case $opt in
        i)
            INPUT=$OPTARG
            ;;
        d)
            DURATION=$OPTARG
            ;;
        u)
            INTERVAL=$OPTARG
            ;;
        *)
            usage
            ;;
    esac
done

# 检查必要的参数是否已提供
if [ -z "$INPUT" ] || [ -z "$DURATION" ] || [ -z "$INTERVAL" ]; then
    usage
fi


HOME_DIR="/home/sx/MPI_profile"
INPUT_DIR="${HOME_DIR}/${INPUT}"
OUTPUT_DIR="${HOME_DIR}/${INPUT}/${DURATION}ms_closed"

echo "Running analysis with the following parameters:"
echo "Input directory: ${INPUT_DIR}"
echo "Output directory: ${OUTPUT_DIR}"
echo "Duration: ${DURATION}ms"
echo "Interval: ${INTERVAL}ms"

echo "Duration: $(( DURATION * 2500000 ))"
echo "Interval: $(( INTERVAL * 2500000 ))"

mkdir ${TRACE_DIR}/${INPUT}
mkdir ${OUTPUT_DIR}

# timeslice_analysis -i ${INPUT_DIR}/trace -f -o ${OUTPUT_DIR}/graph -d /home/sx/MPI_profile/lulesh_8_abnormal/lulesh_lineinfo -l $((INTERVAL * 2500000 )) -u $(( DURATION * 2500000 ))
# timeslice_analysis -i ${INPUT_DIR}/trace -f -o ${OUTPUT_DIR}/graph_edge -d /home/sx/MPI_profile/lulesh_8_abnormal/lulesh_lineinfo -l $(( INTERVAL * 2500000 )) -u $(( DURATION * 2500000 )) -e
# timeslice_analysis -i ${INPUT_DIR}/trace -f -o /home/xzb/data-stad/backtrace/lammps_1024_backtrace -d /home/xzb/MPI_profile/lmp_lineinfo -s /home/xzb/MPI_profile/lammps_1024_abnormal_inject/lammps_1024_abnormal_inject_indices.txt -l $(( INTERVAL * 2500000 )) -u $(( DURATION * 2500000 )) -b