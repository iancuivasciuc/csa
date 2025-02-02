.section .note.GNU-stack,"",@progbits

.data
    text1: .asciz "Text 1\n"
    text2: .asciz "Text 2\n"

    x: .long 5
    y: .long -3

.text
.global main
main:
    movl x, %eax
    movl y, %ebx
    cmp %ebx, %eax
    jg write2

    movl $4, %eax
    movl $1, %ebx
    movl $text1, %ecx
    movl $8, %edx
    int $0x80

    jmp exit

write2:
    movl $4, %eax
    movl $1, %ebx
    movl $text2, %ecx
    movl $8, %edx
    int $0x80

exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
