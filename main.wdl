import "other1.wdl" as other1
import "other2.wdl" as other2

workflow DemoWorkflow {

    Int num_rows
    Int num_cols

    call other1.task1 as t1 {
        input:
            num_rows = num_rows,
            num_cols = num_cols
    }

    call other2.task2 as t2 {
        input:
            num_rows = num_rows,
            num_cols = num_cols
    }

    call merge {
        input:
            f1 = t1.fout,
            f2 = t2.fout
    }

    output {
        File f1 = merge.fout
    }
}

task merge {
    File f1
    File f2

    Int disk_size = 20
    String output_filename = 'final.tsv'

    command {
        python3 /opt/software/concat.py -o ${output_filename} ${f1} ${f2}
    }

    output {
        File fout = "${output_filename}"
    }

    runtime {
        docker: "blawney/merge_mtx"
        cpu: 1
        memory: "4 G"
        disks: "local-disk " + disk_size + " HDD"
        preemptible: 0
    }
}
