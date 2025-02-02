.section .note.GNU-stack,"",@progbits

.data
    x: .space 4
    y: .space 4
    ans: .space 4

    formatScanf: .asciz "%d %d"
    formatPrintf: .asciz "Rezultatul este %d!"
    newLine: .asciz "\n"

.text
sub:
    movl 4(%esp), %eax
    subl 8(%esp), %eax
    movl 12(%esp), %ebx
    movl %eax, (%ebx)

    ret

.global main
main:
    pushl $y
    pushl $x
    pushl $formatScanf
    call scanf
    popl %ebx
    popl %ebx
    popl %ebx

    pushl $ans
    pushl y
    pushl x
    call sub
    popl %ebx
    popl %ebx
    popl %ebx

    pushl ans
    pushl $formatPrintf
    call printf
    popl %ebx
    popl %ebx

    pushl $newLine
    call printf
    popl %ebx

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
