class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        // if(obstacleGrid[m-1][n-1]==1 || obstacleGrid[0][0]==1) return 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                // Base conditions
                if (obstacleGrid[i][j] == 1) {
                    // If there's an obstacle, no paths can pass through it
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 && j == 0) {
                    // Starting point has exactly one path
                    dp[i][j] = 1;
                    continue;
                }

                int up = 0;
                int left = 0;

                // Check if we can move up and left
                if (i > 0)
                    up = dp[i - 1][j];
                if (j > 0)
                    left = dp[i][j - 1];

                // Sum of paths from above and left
                dp[i][j] = up + left;

            }
        }
        return dp[m-1][n-1];
    }
}