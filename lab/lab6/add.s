.section .note.GNU-stack,"",@progbits

.data
    x: .long 5
    y: .long 7
    ans: .space 4

    formatPrintf: .asciz "Rezultatul este %d!"
    newLine: .asciz "\n"

.text
add:
    pushl %ebp
    movl %esp, %ebp

    movl 8(%ebp), %eax
    addl 12(%ebp), %eax

    popl %ebp
    ret

.global main
main:
    pushl x
    pushl y
    call add
    popl %ebx
    popl %ebx

    movl %eax, ans # Rezultatul functiei add este intors in %eax

    pushl ans
    pushl $formatPrintf
    call printf
    popl %ebx
    popl %ebx

    pushl $newLine
    call printf
    popl %ebx

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
