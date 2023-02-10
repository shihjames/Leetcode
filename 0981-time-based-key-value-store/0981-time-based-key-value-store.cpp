class TimeMap {
public:
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        timeMap[key].push_back(make_pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        if (timeMap.find(key) == timeMap.end()) {
            return "";
        }
        
        int left = 0, right = timeMap[key].size() - 1, mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (timeMap[key][mid].first == timestamp) {
                return timeMap[key][mid].second;
            } else if (timeMap[key][mid].first > timestamp) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        if (right >= 0) {
            return timeMap[key][right].second;
        } else {
            return "";
        }
    }

private:
    unordered_map<string, vector<pair<int, string>>> timeMap;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */