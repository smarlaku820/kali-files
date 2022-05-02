# OSI Model

Application Layer
Presentation Layer
Sessions Layer
Transport Layer
Network Layer
Datalink Layer
Physical Layer

APSTNDP - Acronym - Andhra Pradesh Strikes Tamil Nadu Display Picture

### Application Layer
- It is interface to programs running on a computer. 
- It provides networking options for the programs to transmit data.
- The data is passed down to presentation layer.

### Presentation Layer
- This data tends to be in the format that the application layer understands, but its not necessarily in a standardised format that could be understood by the application layer in the receiving computer.
- The presentation layer translates the data into a standardised format, as well as handles encryption, compression or other transformations to the data. 
- The data is then passed down to the sessions layer.

### Sessions Layer
- When the sessions layer receives the correctly formatted data, it looks to see if it can establish a connection with the receiving computer. If it cannot, a error is produced and the message goes no further.
- If a session is established, then its the responsibility of the sessions layer to maintain the session as well as cooperate with the sessions layer of the remote computer to syncrhonize communications.
- Every session created is unique to the communication in question, this is what allows multiple requests to different endpoints simultaneously without the data getting mixed up.(Two browser tabs)
- When the session layer has logged a connection between the remote computer and the host, the data is passed down to Transport layer.

### Transport Layer
- Chooses the protocol over which data is transmitted
- Two most common protocols are TCP & UDP.
- TCP is connection-oriented and relaible.
- UDP is connection-less and unreliable.
- TCP is chosen when accuracy is preffered over speed.
- UDP is often chosen when speed is more important.
- With the protocol selected, the transport layer then divides the transmission into bite-sized pieces, which makes it easier to transmit the message successfully.
- Over TCP it is called segments, over UDP it is called datagrams.

### Network Layer
- Network layer is responsible for locating the destination of your request.
- Routing is handled at this layer & is often associated with the logical addressing of the transmission

### Datalink Layer
- This layer focuses on physical addressing of the transmission
- This layer also checks for data corruption & ensures that it is in the right format.
- This layer is responsible for ensuring the data is formatted for transmission.

### Physical Layer
- The physical layer is right down to the hardware of the computer.
- It is the responsibility of the physical layer to convert the binary data into signals and also responsible for converting the incoming signals back to binary data.
- Physical layer is responsible for transmitting and receiving the data.


## Encapsulation

Layer 7 ---------->                                                      | L7 Header | Data |
Layer 6 ---------->                                          | L6 Header |        Data      |
Layer 5 ---------->                              | L5 Header |           Data               |
Layer 4 ---------->                   L4 Header  |       Data (Segments/DataGrams)          |
Layer 3 ---------->          L3 Header|          Data (Packets)                             |
Layer 2 ----------> L2 Header|                   Data (Frames)                              | L2 Trailer |
Layer 1 ----------> |                            Data Stream (Bits)                                      |

- Data link layer is the only layer in OSI model that adds a trailer during encapsulation
- The receiving computer will perform a de-encapsulation.

## TCP/IP Model

------------------------------------------------
   OSI Model        |  TCP/IP Model
------------------------------------------------
Application Layer   |
Presentation Layer  |  Application Layer
------------------------------------------------
Sessions Layer      |
Transport Layer     |  Transport Layer
Network Layer       |  Internet Layer
------------------------------------------------
Data link Layer     |
Physical Layer      |  Network Interface Layer
------------------------------------------------
