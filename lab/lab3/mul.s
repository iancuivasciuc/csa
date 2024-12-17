.section .note.GNU-stack,"",@progbits

.data
    x: .long 30
    y: .long 7
.text
.global main
main:
    mov x, %eax
    mov y, %ebx

    add %eax, %ebx // %ebx = x + y

    mov x, %eax
    mov y, %ebx
    sub %eax, %ebx // %ebx = x - y

    mov x, %eax
    mov y, %ebx
    mul %ebx // %eax = x * y


    mov $1, %eax
    mov $0, %ebx
    int $0x80

