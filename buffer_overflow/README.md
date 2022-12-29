# Illustration of buffer overflow concepts

- Let us try to run a simple C program which will demonstrate buffer overflow.
- Since this is a 64 bit VM, we need to compile the C program so that it will be run as 32 bit program.
- Run the following command to compile the C program and provide certain flags to remove overflow protection mechanisms.
  `gcc -o buffer_overflow -fno-stack-protector -z execstack -m32 <buffer_overflow.c>`
- Also you need to set the following at the kernel level
  `echo "0" > /proc/sys/kernel/randomize_va_space`

## Demonstrating the buffer overflow

```

The difference between buf1 and buf2 is 16 bytes.
So the size is 16 bytes as it is allocated by the char buffer.

First buf2 will be allocated and then buf1 will be allocated in contigous allocations in the stack.

In the first case, buf2 has 15 A's and finally it is terminated by the Null character.

┌──(root㉿kali)-[/home/bluejay820/Documents/kali-files/buffer_overflow]
└─# ./buffer_overflow
Enter something for buf2:AAAAAAAAAAAAAAA
Value at buf1: secret
Value at buf2: AAAAAAAAAAAAAAA
Address at buf1: 0xfffffffff250
Address at buf2: 0xfffffffff240
                                                                                      

In the second case, buf2 has 16 A's and since it has to be terminated by the null character, thats get overwritten
into the next variable which is buf1 and hence you cannot see anything in the buf1                                        

┌──(root㉿kali)-[/home/bluejay820/Documents/kali-files/buffer_overflow]
└─# ./buffer_overflow
Enter something for buf2:AAAAAAAAAAAAAAAA
Value at buf1: 
Value at buf2: AAAAAAAAAAAAAAAA
Address at buf1: 0xfffffffff250
Address at buf2: 0xfffffffff240

In the third case, buf2 has 17 A's and now you can see its rolling onto the next variable buf1 the extra additional A with its null character.                                                                                                                              
                                                                                                                              
┌──(root㉿kali)-[/home/bluejay820/Documents/kali-files/buffer_overflow]
└─# ./buffer_overflow
Enter something for buf2:AAAAAAAAAAAAAAAAA
Value at buf1: A
Value at buf2: AAAAAAAAAAAAAAAAA
Address at buf1: 0xfffffffff250
Address at buf2: 0xfffffffff240
```
