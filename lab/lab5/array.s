.section .note.GNU-stack,"",@progbits

# Program care calculeaza indexul ultimului element din array care este divizibil cu 3

.data
    n: .long 6
    v: .word 5, 12, 7, 4, 9, 2 # Array de 6 worduri (12 de bytes in total)
    ans: .long -1
.text
.global main
main:
    lea v, %esi # Muta adresa lui v in %esi
    movl $3, %ebx
    xorl %ecx, %ecx

etloop:
    cmpl n, %ecx
    je etexit

    xorl %eax, %eax
    movw (%esi, %ecx, 2), %ax # Muta elementul de la indexul %ecx in %eax
    xorl %edx, %edx # Inainte sa fac impartirea, ma asigur ca %edx este gol
    divl %ebx

    cmpl $0, %edx # Daca restul impartii este 0, updatez indexul
    je etupdate

etinloop:
    incl %ecx
    jmp etloop

etupdate:
    movl %ecx, ans # Mut indexul curent in rezultat
    jmp etinloop # Ma intorc in loop

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
