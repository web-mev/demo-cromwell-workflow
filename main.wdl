workflow DemoWorkflow {

    File f1
    File f2

    call concat {
        input:
            f1 = f1,
            f2 = f2
    }

    output {
        File output = concat.fout
    }
}

task concat {
    File f1
    File f2

    Int disk_size = 10
    String output_filename = 'final.txt'

    command {
        cat ${f1} ${f2} > ${output_filename}
    }

    output {
        File fout = "${output_filename}"
    }

    runtime {
        docker: "docker.io/ubuntu:bionic"
        cpu: 1
        memory: "4 G"
        disks: "local-disk " + disk_size + " HDD"
    }
}
