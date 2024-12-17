.section .note.GNU-stack,"",@progbits

.data
    x: .long 17
    y: .long 6
.text
.global main
main:
    movl $1, %edx
    movl x, %eax
    jmp et
    mov $0, %edx
et:
    divl y
label:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
