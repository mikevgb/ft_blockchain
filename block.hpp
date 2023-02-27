#ifndef BLOCK_HPP
#define BLOCK_HPP

#include <iostream>

class Block
{
    private:
    int _index;
    time_t _timestamp;
    std::string _data;
    std::string _previousHash;
    size_t _hash;
    std::hash<std::string> _behash;
    int _nonce;

    public:
    Block(int index, int timestamp, std::string data, std::string previousHash) : 
        _index(index), _timestamp(timestamp), _data(data), _previousHash(previousHash) 
    {
        calculateHash();
        _nonce = 0;
    };
    virtual ~Block() {};
    void calculateHash()
    {
        std::string _stringBeforeHashing = std::to_string(_nonce) + std::to_string(_index) + std::to_string(_timestamp) + _data + _previousHash;
        _hash = _behash(_stringBeforeHashing);
    };
    size_t getHash() { return _hash; };
    void mineBlock(int difficulty)
    {
        //std::cout << std::to_string(_hash).substr(0, difficulty) << std::endl;
        //std::cout << std::to_string(4) << std::endl;
        while(std::to_string(_hash).substr(0, difficulty) != std::to_string(4))
        {
            calculateHash();
            //std::cout << "hash " << _hash << std::endl;
            _nonce++;
            //std::cout << "nonce " << _nonce << std::endl;
        }
        std::cout << "block mined!" << std::endl;
    };
   
};

#endif


// ref:
// https://akshaykore.medium.com/building-a-blockchain-7579c53962dd
// https://blog.gameoflife.co/implementing-a-simple-proof-of-work-algorithm-for-the-blockchain-bdcd50faac18