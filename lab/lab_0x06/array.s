.section .note.GNU-stack,"",@progbits

.data
    n: .space 4   # Number of elements
    v: .space 400 # Array with max 100 longs (400 bytes = 100 * 4)

    format_scanf: .asciz "%d"
    format_printf: .asciz "%d "
    newline: .asciz "\n"

.text
.global main
main:
    # Read n
    pushl $n
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    # Load array base address into %edi
    leal v, %edi

    # Initialize counter to 0
    xorl %ecx, %ecx

et_read_loop:
    # Stop after all n elements have been read
    cmpl n, %ecx
    je et_print

    # Save counter (every call will probably modify %eax, %ecx, %edx)
    pushl %ecx

    # ########################################################################################### #
    #                                                                                             #
    # (%edi, %ecx, 4) -> Computes the address %edi + %ecx * 4 (typically used for accessing v[i]) #
    #                                                                                             #
    # leal (%edi, %ecx, 4), %eax -> Computes the address %edi + %ecx * 4 and stores it in %eax    #
    #                                                                                             #
    # movl (%edi, %ecx, 4), %eax -> Loads the value at address %edi + %ecx * 4 into %eax          #
    #                                                                                             #
    # ########################################################################################### #
    leal (%edi, %ecx, 4), %eax

    # Push the address where scanf will store the input value
    pushl %eax
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    # Restore counter
    popl %ecx

    # Increment counter
    incl %ecx
    jmp et_read_loop

et_print:
    # Print n
    pushl n
    pushl $format_printf
    call printf
    popl %eax
    popl %eax

    # Print newline
    pushl $newline
    call printf
    popl %eax

    # Reset counter to 0
    xorl %ecx, %ecx

et_print_loop:
    # Stop after all n elements have been printed
    cmpl n, %ecx
    je et_print_newline

    # Save counter
    pushl %ecx

    # Push the value of v[i]
    pushl (%edi, %ecx, 4)
    pushl $format_printf
    call printf
    popl %eax
    popl %eax

    # Restore counter
    popl %ecx

    # Increment counter
    incl %ecx
    jmp et_print_loop

et_print_newline:
    # Print newline
    pushl $newline
    call printf
    popl %eax

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
