.section .note.GNU-stack,"",@progbits

.data
    n: .long 10
    fibo1: .long 0
    fibo2: .long 1

.text
.global main
main:
    movl $2, %ecx

etloop:
    cmp n, %ecx
    ja etexit

    movl fibo1, %eax
    addl fibo2, %eax
    
    movl fibo2, %ebx
    movl %ebx, fibo1
    movl %eax, fibo2

    addl $1, %ecx
    jmp etloop

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
