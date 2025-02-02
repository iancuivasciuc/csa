.section .note.GNU-stack,"",@progbits

.data
    directory: .asciz "/home/iancu/Desktop/university/assistant/2024/asc/lab/lab11"
    format_printf: .asciz "Name: %s!\n"

.text
.global main
main:
    pushl $directory
    call opendir
    addl $4, %esp

    movl %eax, %ebx

et_readdir:
    pushl %ebx
    call readdir
    addl $4, %esp
    
    cmp $0, %eax
    je et_exit

    addl $11, %eax

    pushl %eax
    pushl $format_printf
    call printf
    addl $8, %esp

    incl %ecx
    jmp et_readdir

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
