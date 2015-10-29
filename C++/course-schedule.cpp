class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::pair<int, int>> &prerequisites) {
        std::unordered_map<int, int> degrees;
        std::vector<std::vector<int>> edges(numCourses, std::vector<int>());
        std::stack<int> sources;
        for(int i=0; i<numCourses; ++i) degrees[i]=0;
        for(auto p : prerequisites) {
            ++degrees[p.first];
            edges[p.second].push_back(p.first);
        }
        for(int i=0; i<numCourses; ++i) {
            if(degrees[i]==0)
                sources.push(i);
        }
        while(!sources.empty()) {
            int n = sources.top();
            sources.pop();
            
            for(auto m : edges[n]) {
                --degrees[m];
                if(degrees[m]<=0)
                    sources.push(m);
            }
            edges[n].clear();
        }
        for(auto e : edges) {
            if(!e.empty())
                return false;
        }
        return true;
    }
};
