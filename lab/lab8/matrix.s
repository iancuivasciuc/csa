.section .note.GNU-stack,"",@progbits

.data
    n: .space 4
    m: .space 4
    matrix: .space 40000
    i: .long 0
    j: .long 0

    format_scanf: .asciz "%d"
    format_printf: .asciz "%d "
    new_line: .asciz "\n"

.text
.global main
main:
    # Input value for n
    pushl $n
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    # Input value for m
    pushl $m
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    lea matrix, %edi
    xorl %ecx, %ecx

    movl n, %eax
    mull m
    movl %eax, %ebx # Store n * m in %ebx

et_read:
    cmpl %ebx, %ecx
    je et_after_read

    # Save %ecx to the stack to preserve its value
    pushl %ecx

    # Calculate address of matrix[i][j] and store in %eax
    lea (%edi, %ecx, 4), %eax

    # Input value for matrix[i][j]
    pushl %eax
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    # Restore %ecx from the stack
    popl %ecx

    incl %ecx
    jmp et_read

et_after_read:
    movl $0, i
    xorl %ecx, %ecx

et_print_i:
    # Loop over rows
    cmpl %ebx, %ecx
    je et_exit

    movl $0, j

et_print_j:
    # Loop over columns
    movl j, %edx
    cmpl %edx, m
    je et_incl_i

    # Save %ecx to the stack to preserve its value
    pushl %ecx

    # Output the value of matrix[i][j]
    pushl (%edi, %ecx, 4)
    pushl $format_printf
    call printf
    popl %eax
    popl %eax

    # Restore %ecx from the stack
    popl %ecx

    incl %ecx
    incl j
    jmp et_print_j

et_incl_i:
    # Save %ecx to the stack to preserve its value
    pushl %ecx

    # Output a newline character
    pushl $new_line
    call printf
    popl %eax

    # Restore %ecx from the stack
    popl %ecx

    incl i
    jmp et_print_i

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
