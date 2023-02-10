class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) {
            return false;
        }

        int rows = matrix.size(), cols = matrix[0].size();
        int left = 0, right = rows * cols - 1, mid, row, col;

        while (left <= right) {
            mid = left + (right - left) / 2;
            row = mid / cols;
            col = mid % cols;
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return false;
    }
};