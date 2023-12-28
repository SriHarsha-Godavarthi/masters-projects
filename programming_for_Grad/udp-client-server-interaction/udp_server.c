#include <stdio.h> // has the declarations used by standard input and output
#include <sys/types.h> // contains definitions of data types used in system calls by socket.h and in.h
#include <sys/socket.h> // contains definitions of structures needed for sockets 
#include <netinet/in.h> // contains constants and structures needed for internet and domain addresses
#include <stdlib.h> // defines four variable types and several macros,various functions for performing general functions
#include <string.h> // for using string functions
#include <unistd.h>
#include <time.h> // for using time
#define BUFFER_SIZE 1024

void error(const char *msg) {
    // this function is used to print error messages and exit program
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[]) {
    
    if (argc < 2) {
        //argc - will store no of arguments passed
        // check if port is passed as argument
        fprintf(stderr, "Port No not provided. Terminate.\n");
        //exit program
        exit(1);
    }
    //declare socket descriptor,port number,n - flag checking if any error occured
    int sockfd, portno, n;
    // declare the message to store
    char buffer[BUFFER_SIZE];
    // create address structure for server and client
    struct sockaddr_in6 serv_addr, cli_addr;
    // to store client length
    socklen_t clilen;
   // create socket with ipv6 and UDP protocol
    
    sockfd = socket(AF_INET6, SOCK_DGRAM, 0);

    /* explanation for socket function
    domain for ipv4 - AF_INET
    domain for ipv6 - AF_INET6
    type for tcp - SOCK_STREAM
    type for udp - SOCK_DGRAM
    protocal by default 0 for tcp
    */


    if (sockfd < 0) {
        error("Error opening socket.");
    }
    // empty the server address 
    bzero((char *)&serv_addr, sizeof(serv_addr));
    //atoi() - convert port number to integer
    portno = atoi(argv[1]);
    //configure host,port,protocol for server
    serv_addr.sin6_family = AF_INET6;
    serv_addr.sin6_addr = in6addr_any;
    serv_addr.sin6_port = htons(portno);
    /*bind the socket to the port specified if fails throw error and exit*/
    /* int bind(int sockfd,const struct sockadrr *serveraddr,serveaddrlen) 
    this function binds filedescriptor generated from above socket function and binds it

    return 0 if bind is successfull (or) -1 if failed to bind
    sockfd – File descriptor of a socket to be bonded 
    serveraddr – Structure in which the address to be bound to is specified 
    serveaddrlen – Size of addr structure  
    */
    if (bind(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        error("Binding failed.");
    }
    // client address size
    clilen = sizeof(cli_addr);
    // continuosly listen for incoming messages from given client and print it
    while (1) {
        bzero(buffer, BUFFER_SIZE);
        //check for any message (or) packets send from client
        // recive package from client using function recvfrom()
        /*
        sockfd - file descriptor
        buffer - buffer 
        BUFFER_SIZE
        flag - 0 
        client_addr
        clientlength
        */
        n = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&cli_addr, &clilen);
        if (n < 0) {
            error("Error while reading.");
        }
         // Get the current time
        time_t currentTime;
        time(&currentTime);
        printf("Packet Received At: %s\n", ctime(&currentTime));
        printf("Client: %s\n", buffer);

        // bzero(buffer, BUFFER_SIZE);
        // fgets(buffer, BUFFER_SIZE, stdin);

        // n = sendto(sockfd, buffer, strlen(buffer), 0, (struct sockaddr *)&cli_addr, clilen);
        // if (n < 0) {
        //     error("Error while writing.");
        // }

        // int i = strncmp("Bye", buffer, 3);
        // if (i == 0)
        //     break;
    }
    // close socket
    close(sockfd);
    return 0;
}
