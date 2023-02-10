class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, double>> posSpeedPairs;
        stack<double> stk;
        
        // make pair
        for (int i = 0; i < speed.size(); i++) {
            double time = (double) (target - position[i]) / speed[i];
            posSpeedPairs.push_back(make_pair(position[i], time));
        }
        
        // sort by position
        sort(posSpeedPairs.begin(), posSpeedPairs.end());

        for (int i = posSpeedPairs.size() - 1; i >= 0; i--) {
            double time = posSpeedPairs[i].second;
            // cannot chase the front car
            if(stk.empty() || time > stk.top()) {
                stk.push(posSpeedPairs[i].second);
            }
        }
        // number of car fleets
        return stk.size();
    }
};