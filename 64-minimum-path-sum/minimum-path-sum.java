class Solution {
    public static int min(int a, int b){
        return Math.min(a,b);
    }
    public int minPathSum(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        int [][]dp = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0 && j==0){
                    dp[i][j]=grid[i][j];
                    continue;
                }
                int top=Integer.MAX_VALUE;
                int left=Integer.MAX_VALUE;
                if(i>0) top = dp[i-1][j];
                if(j>0) left = dp[i][j-1];
                dp[i][j] = grid[i][j]+min(top, left);
            }
        }
        return dp[m-1][n-1];

        
    }
}