#include "blockchain.hpp"
//#include "sys/time.h"
//#include <iostream>
#include <unistd.h>

int main()
{
    //struct timeval current_time;
    Blockchain _elBlock;

    //_elBlock.getHashLastBlock();
    //sleep(1);
    _elBlock.addBlock();
    //_elBlock.getHashLastBlock();
    sleep(1);
    _elBlock.addBlock();
    sleep(1);
    _elBlock.addBlock();
    sleep(1);
    _elBlock.addBlock();
    sleep(1);
    _elBlock.addBlock();
    //_elBlock.getHashLastBlock();
    //sleep(1);
    //_elBlock.addBlock();
    //_elBlock.getHashLastBlock();
    //gettimeofday(&current_time, NULL);
    //int time = current_time.tv_sec;

    //std::cout << time << std::endl;

    return 0;
}