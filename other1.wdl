task task1 {

    Int num_rows
    Int num_cols

    Int disk_size = 20
    String output_filename = 'm1.tsv'

    command {
        python3 /opt/software/create_random_matrix.py \
            -r ${num_rows} \
            -c ${num_cols} \
            -o ${output_filename}
    }

    output {
        File fout = "${output_filename}"
    }

    runtime {
        docker: "blawney/task1"
        cpu: 1
        memory: "4 G"
        disks: "local-disk " + disk_size + " HDD"
        preemptible: 0
    }
}