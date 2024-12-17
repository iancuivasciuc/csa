.section .note.GNU-stack,"",@progbits

.data
    x: .long 23
    formatString: .asciz "Numar: %d!"
    newLine: .asciz "\n"

.text
.global main
main:
    pushl x
    pushl $formatString
    call printf
    popl %ebx
    popl %ebx

    # pushl $0
    # call fflush
    # popl %ebx

    pushl $newLine
    call printf
    popl %ebx

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
