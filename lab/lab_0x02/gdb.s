.section .note.GNU-stack,"",@progbits

.data
.text
.global main
main:
    mov $1, %eax
    mov $2, %ebx

    mov $1, %eax
    mov $0, %ebx
    int $0x80

