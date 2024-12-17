.section .note.GNU-stack,"",@progbits

.data
    x: .space 4
    y: .space 4

    formatPrintf: .asciz "%d "
    formatScanf: .asciz "%d"
    formatScanf2: .asciz "%d %d"
    newLine: .asciz "\n"

.text
.global main
main:
    pushl $x
    pushl $formatScanf
    call scanf
    popl %ebx
    popl %ebx

    pushl x
    pushl $formatPrintf
    call printf
    popl %ebx
    popl %ebx

    # pushl $y
    # pushl $x
    # pushl $formatScanf2
    # call scanf
    # popl %ebx
    # popl %ebx
    # popl %ebx

    # pushl x
    # pushl $formatPrintf
    # call printf
    # popl %ebx
    # popl %ebx

    # pushl y
    # pushl $formatPrintf
    # call printf
    # popl %ebx
    # popl %ebx

    pushl $newLine
    call printf
    popl %ebx

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
