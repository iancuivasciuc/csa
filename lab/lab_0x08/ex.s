.section .note.GNU-stack,"",@progbits

.section .rodata
    format_scanf: .asciz "%d %d"
    format_printf: .asciz "Difference: %d\n"

.data
.text
.global main
main:
    # Create stack frame
    pushl %ebp
    movl %esp, %ebp

    # Make room for two variables on stack
    # -4(%esp) = x
    # -8(%esp) = y
    subl $8, %esp

    # Read x and y
    leal -8(%ebp), %eax
    pushl %eax
    leal -4(%ebp), %eax
    pushl %eax
    pushl $format_scanf
    call scanf
    addl $12, %esp

    movl -4(%ebp), %eax
    subl -8(%ebp), %eax

    # Print x - y
    pushl %eax
    pushl $format_printf
    call printf
    addl $8, %esp

    # Remove variables x and y from the stack
    addl $8, %esp

et_exit:
    popl %ebp

    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
