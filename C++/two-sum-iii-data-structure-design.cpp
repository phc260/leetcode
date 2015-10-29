class TwoSum {
private:
    std::unordered_map<int, int> hashmap;
public:
	void add(int number) {
	    if(hashmap.find(number)==hashmap.end())
	        hashmap[number] = 0;
	    hashmap[number] += 1;
	}

	bool find(int value) {
	    for(auto a : hashmap) {
	        if(hashmap.find(value-a.first)!=hashmap.end()) {
	            if(hashmap[a.first]>1 || a.first*2!=value)
	                return true;
	        }
	    }
	    return false;
	}
};
