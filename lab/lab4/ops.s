.section .note.GNU-stack,"",@progbits

.data
    x: .long 30
    y: .long 7
    sum: .space 4
    dif: .space 4
    prod: .space 4
    cat: .space 4
    rest: .space 4

.text
.global main
main:
    movl x, %eax
    addl y, %eax
    movl %eax, sum # sum = x + y

    movl x, %eax
    subl y, %eax
    movl %eax, dif # dif = x - y

    movl x, %eax
    mull y
    movl %eax, prod # prod = x * y

    movl $0, %edx
    movl x, %eax
    divl y
    movl %eax, cat # cat = x / y
    movl %edx, rest # rest = x % y

exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
