rule helloworld_checker {
     strings:
             $hello_world = "Hello World!"
             $hello_world_lower = "hello world!"
             $hello_world_upper = "HELLO WORLD!"
     condition:
             any of them
}
