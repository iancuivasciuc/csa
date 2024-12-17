.section .note.GNU-stack,"",@progbits

# int prime(int x)
# {
#     if (x < 2)
#         return 0;

#     for (int d = 2; d * d <= x; d++) {
#         if (x % d == 0)
#             return 0;
#     }

#     return 1;
# }

.data
    x: .space 4

    format_scanf: .asciz "%d"
    yes: .asciz "Yes\n"
    no: .asciz "No\n"

.text
prime:
    pushl %ebp
    movl %esp, %ebp

    pushl %ebx

    # Move x to %ebx
    movl 8(%ebp), %ebx

    # If x < 2, than x is not prime.
    cmp $2, %ebx
    jl prime_no

    movl $2, %ecx

prime_loop:
    movl %ecx, %eax
    imul %eax

    cmp %ebx, %eax
    jg prime_yes

    movl %ebx, %eax
    xorl %edx, %edx

    idiv %ecx

    cmp $0, %edx
    je prime_no

    incl %ecx
    jmp prime_loop

prime_yes:
    # The x is prime
    movl $1, %eax
    jmp prime_end

prime_no:
    # The x is not prime
    xorl %eax, %eax

prime_end:
    popl %ebx
    popl %ebp
    ret

.global main
main:
    # Read x
    pushl $x
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    pushl x
    call prime
    popl %ebx

    cmp $0, %eax
    je et_no

    # Print Yes
    pushl $yes
    call printf
    popl %eax
    jmp et_exit

et_no:
    # Print No
    pushl $no
    call printf
    popl %eax

et_exit:
    pushl $0
    call fflush
    popl %eax

    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
