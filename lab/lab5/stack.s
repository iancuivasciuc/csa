.section .note.GNU-stack,"",@progbits

.data
.text
.global main

# func (x, y, z, &rez); rez = (x - y) * z;

main:
    pushl $1
    pushw $2
    pushl $3

    movl (%esp), %eax # 3

    xorl %ebx, %ebx
    movw 4(%esp), %bx # 2

    movl 6(%esp), %ecx # 1

    popl %ecx
    popw %cx
    popl %ecx

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
