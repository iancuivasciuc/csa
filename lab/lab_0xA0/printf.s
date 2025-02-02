.data
    x: .long 0
    y: .long 0
    format_scanf: .asciz "%d %d"
    format_printf: .asciz "My numbers are %d %d!\n"

.text
.global main
main:
    pushl $y
    pushl $x
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax
    popl %eax

    pushl y
    pushl x
    pushl $format_printf
    call printf
    popl %eax
    popl %eax
    popl %eax

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
