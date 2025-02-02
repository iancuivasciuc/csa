.section .note.GNU-stack,"",@progbits

.data
    x: .word 15
    y: .word 7

.text
.global main
main:
    // Wrong
    // mov x, %eax

    // Right
    movl $0, %eax
    movw x, %ax

exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
