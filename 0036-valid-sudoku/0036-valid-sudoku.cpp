class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool row[9][9] = {false};
        bool col[9][9] = {false};
        bool block[9][9] = {false};

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                char cur = board[i][j];
                if (cur == '.') {
                    continue;
                }

                int idx = cur - '1';
                int area = (i / 3) * 3 + j / 3;

                if (row[i][idx] || col[j][idx] || block[area][idx]) {
                    return false;
                }

                row[i][idx] = true;
                col[j][idx] = true;
                block[area][idx] = true;
            }
        }
        
        return true;
    }
};