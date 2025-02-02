.section .note.GNU-stack,"",@progbits

.data
    x: .long 0x000DB000
    y: .long 327

    pal: .asciz "Palindrome!\n"
    notpal: .asciz "No palindrome!\n"

.text
.global main
main:
    movl x, %eax # Use the %eax register to build x reversed in %ebx
    xorl %ebx, %ebx
    movl $32, %ecx # 32 because I will add bit by bit. There are 32 bits inside a register

etloop:
    movl %eax, %edx
    andl $1, %edx # Now, %edx holds the LSB of %eax
    shrl $1, %eax # Move to the next bit

    shll $1, %ebx # Make space for the bit that will be added
    addl %edx, %ebx # Add the LSB of %eax to %ebx
    loop etloop

    cmp x, %ebx
    jne etnotpal # If the original x and %ebx are not equal, it means that x is not a palindrome

    movl $4, %eax
    movl $1, %ebx
    movl $pal, %ecx
    movl $13, %edx
    int $0x80 # Print pal message

    jmp etexit

etnotpal:
    movl $4, %eax
    movl $1, %ebx
    movl $notpal, %ecx
    movl $16, %edx
    int $0x80 # Print notpal message

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
