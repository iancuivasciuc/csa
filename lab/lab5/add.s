.section .note.GNU-stack,"",@progbits

.data
    x: .long 5
    y: .long 3
    z: .long 4
    s: .space 4

.text

# add(x, y, &s);
add:
    movl 4(%esp), %eax
    subl 8(%esp), %eax # %eax = x - y
    mull 12(%esp) # %eax = (x - y) * z
    movl 16(%esp), %ebx # %ebx = $s
    movl %eax, (%ebx) # s = (x - y) * z

    ret

.global main
main:
    pushl $s
    pushl z
    pushl y
    pushl x
    call add

et:
    popl %eax
    popl %ebx
    popl %edx
    popl %edx

etexit:
    movl $1, %eax
    xor %ebx, %ebx
    int $0x80
