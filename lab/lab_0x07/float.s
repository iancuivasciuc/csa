.data
    number: .float 2.718281828
    logResult: .space 4

.text
.global main
main:
    # FPU
    flds number # Load the value of FPU stack

    subl $4, %esp
    fstps 0(%esp) # Push the float value on stack
    call logf
    popl %ebx # Pop stack

    fstps logResult # The result is in st(0)

    # SSE
    # subl $4, %esp                     # Make space on the stack for the float
    # movss number, (%esp)     
    # call logf
    # addl $4, %esp

    # movss %xmm0, logResult

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
