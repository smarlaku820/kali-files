# the file must be a text file
rule helloworld_checker {
     strings:
             $hello_world = "Hello World!"
             $txt_file = "*.txt"
     condition:
             $hello_world and $txt_file
}
