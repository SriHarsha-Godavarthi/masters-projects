#include<stdio.h> // has the declarations used by standard input and output
#include<sys/types.h> // contains definitions of data types used in system calls by socket.h and in.h
#include<sys/socket.h>
#include<netinet/in.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<netdb.h>
#include <time.h>
#define BUFFER_SIZE 1024

void error(const char *msg) {
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s hostname port\n", argv[0]);
        exit(1);
    }

    int sockfd, portno, n;
    char buffer[BUFFER_SIZE];
    struct sockaddr_in serv_addr;
    struct hostent *server;
    // create file pointer
    FILE *file;
    // open a file
    file = fopen("hw6input.txt", "r");
     // Check if the file was opened successfully
     
    if (file == NULL) {
        perror("Error opening the file");
        exit(1);
    }
    // assign port number to listen
    portno = atoi(argv[2]);
    // create udp socket with ipv6
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        error("Error opening socket.");
    }
    //get host name
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr, "Error: no such host\n");
        exit(1);
    }
    // configure protocols
    bzero((char *)&serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
    serv_addr.sin_port = htons(portno);
    
    
    // read until no content is left in file
    while (fgets(buffer, sizeof(buffer), file)) {
        // Get the current time
        time_t currentTime;
        time(&currentTime);
        // Convert hexadecimal to integer and storing it in buffer
        sprintf(buffer, "%ld", strtol(buffer, NULL, 16));
        printf("sending packet: %s\n",buffer);
        printf("Packet Send At: %s\n", ctime(&currentTime));
        // send packets to server
        n = sendto(sockfd, buffer, strlen(buffer), 0, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
        if (n < 0) {
            error("Error on Sending buffer");
            // exit(1);
        }
        bzero(buffer, BUFFER_SIZE);
        // wait for 10 seconds
        sleep(10);
        // bzero(buffer, BUFFER_SIZE);
        // socklen_t len = sizeof(serv_addr);
        // n = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&serv_addr, &len);
        // if (n < 0) {
        //     error("Error on reading");
        // }

        // printf("Server: %s", buffer);

        // int i = strncmp("Bye", buffer, 3);
        // if (i == 0) {
        //     break;
        // }
    }
    // close file
    fclose(file);
    //close socket connection
    close(sockfd);
    return 0;
}
