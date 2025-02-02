.section .note.GNU-stack,"",@progbits

# Register classification in x86:
# 
# Callee-saved registers: %ebx, %edi, %esi, %ebp, %esp.
# - These registers must be preserved by the callee function.
# - If a function modifies these registers, it is responsible for saving their original values at the beginning of the function 
#   (usually by pushing them onto the stack) and restoring them before returning.
# - For example:
#     pushl %ebx           # Save original value of %ebx
#     ... (use %ebx for computations)
#     popl %ebx            # Restore original value before returning
# - This ensures that the calling function can rely on these registers having the same values after the function call as before.

# Caller-saved registers: %eax, %ecx, %edx.
# - These registers may be overwritten during a function call.
# - If a caller function needs to preserve the values in these registers, it must save them before making a function call
#   (e.g., by pushing them onto the stack) and restore them afterward.
# - For example:
#     pushl %eax           # Save current value of %eax
#     call some_function   # Call may overwrite %eax
#     popl %eax            # Restore original value of %eax
# - The caller must assume that any of these registers could be changed by the called function.

.data
    n: .space 4                       # Storage for input number

    format_scanf: .asciz "%d"         # Format string for scanf
    format_printf: .asciz "%d\n"      # Format string for printf

.text
# Function to compute the factorial of an integer using recursion:
# int factorial(int n)
# {
#     if (n == 0)
#         return 1;
#     return n * factorial(n - 1);
# }

# Function: factorial(int n)
# Computes n! recursively. Result is returned in %eax.
factorial:
    # Create stack frame
    pushl %ebp
    movl %esp, %ebp

    pushl %ebx                        # Save callee-saved %ebx

    movl 8(%ebp), %ebx                # Get n (argument is at offset 8 from %ebp)

    # Base case: if (n == 0), return 1
    cmp $0, %ebx
    je factorial_case_zero

    # Recursive case: n * factorial(n - 1)
    movl %ebx, %eax                   # Copy n to %eax
    decl %eax                         # %eax = n - 1

    pushl %eax                        # Push argument for recursive call
    call factorial                    # Call factorial(n - 1)
    popl %edx                         # Restore stack (remove argument)

    imul %ebx                         # Multiply %ebx (n) with %eax (result of factorial(n - 1))
    jmp factorial_exit                # Skip base case return

factorial_case_zero:
    movl $1, %eax                     # Return 1 for factorial(0)

factorial_exit:
    popl %ebx                         # Restore saved %ebx
    popl %ebp                         # Restore saved %ebp
    ret                               # Return to caller

# Entry point: main()
.global main
main:
    # Read input: scanf("%d", &n)
    pushl $n
    pushl $format_scanf
    call scanf
    popl %eax
    popl %eax

    # Compute factorial(n)
    pushl n
    call factorial
    popl %ebx

    # Print result: printf("%d\n", factorial(n))
    pushl %eax
    pushl $format_printf
    call printf
    popl %eax
    popl %eax

et_exit:
    # Flush
    pushl $0
    call fflush
    popl %eax

    # Exit program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
