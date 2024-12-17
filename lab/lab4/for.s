.section .note.GNU-stack,"",@progbits

# int main()
# {
#     int n = 5, s = 0;
# 
#     for (int i = 0; i < n; i++)
#     {
#         s += i;
#     }
#
#     printf("%d\n", s);
#     return 0;
# }

.data
    n: .long 5
    s: .long 0
.text
.global main
main:
    xorl %ecx, %ecx

etloop:
    # daca %ecx == n, am terminat parcurgerea, sarim la exit
    cmp n, %ecx
    je exit

    # s += %ecx
    addl %ecx, s

    # %ecx += 1
    addl $1, %ecx

    # reiau parcurgerea
    jmp etloop

exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
