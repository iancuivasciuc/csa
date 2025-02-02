.section .note.GNU-stack,"",@progbits

.data
    x: .byte 0

.text
.global main
main:
    movb $-8, x
    shrb $1, x

    movb $-8, x
    sarb $1, x
    
exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
