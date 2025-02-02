.section .note.GNU-stack,"",@progbits

.data
    x: .long 30
    y: .long 7
    ans1: .space 4

.text
.global main
main:
    mov x, %eax
    mov $3, %ebx
    mul %ebx // %eax = 3 * x
    mov %eax, ans1 ans1 = 3 * x

    mov y, %eax
    mov $2, %ebx
    mul %ebx // %eax = 2 * y

    add %eax, ans1 // ans1 = 3 * x + 2 * y

exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
