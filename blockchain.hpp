#ifndef BLOCKCHAIN_HPP
#define BLOCKCHAIN_HPP

#include <iostream>
#include "block.hpp"
#include <vector>
#include "sys/time.h"

class Block;

class Blockchain
{
    private:
    std::vector<Block> _block;
    int _index;
    struct timeval current_time;
    int _time;
    int _difficulty;

    public:
    Blockchain() 
    {
        _index = 0;
        _time = 0;
        _difficulty = 1;
        genesisBlock();
    };
    virtual ~Blockchain() {};
    Block genesisBlock()
    {
        _block.push_back(Block(_index, _time, "Genesis Block", "0"));
        printStatus();
        return _block.at(0);
    };
    Block getLatestBlock()
    {
        int pos = _block.size() - 1;
        return _block.at(pos);
    };
    void addBlock()
    {
        //_block[_index].mineBlock(_difficulty);
        _index++;
        _difficulty++;
        getTime();
        _block.push_back(Block(_index, 1, "Another Block", std::to_string(getLatestBlock().getHash())));
        printStatus();
    };
    void printStatus()
    {
        int pos = _index;
        std::cout << "idx: " << _index << " hash: " << _block[pos].getHash() << "\r";
        std::cout.flush();
    };
    void getTime()
    {
        gettimeofday(&current_time, NULL);
        _time = current_time.tv_sec;
    };
    int getDiff() { return _difficulty; };
};

#endif