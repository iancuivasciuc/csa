.section .note.GNU-stack,"",@progbits

.data
    hello: .asciz "Hello, World!\n"

.text
.global main
main:
    mov $4, %eax
    mov $1, %ebx
    mov $hello, %ecx 
    mov $15, %edx
    int $0x80

    mov $1, %eax
    mov $0, %ebx
    int $0x80
