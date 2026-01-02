class Solution {
        public static int min(int a, int b, int c){return Math.min(a,Math.min(b,c));}
    public int minFallingPathSum(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int [][]dp = new int[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0){
                    dp[i][j] = matrix[i][j];
                    continue;
                }
                int top_left=Integer.MAX_VALUE;
                int top=Integer.MAX_VALUE;
                int top_right=Integer.MAX_VALUE;
                if(j>0){
                    top_left=dp[i-1][j-1];
                }
                if(j<n-1){
                    top_right=dp[i-1][j+1];
                }
                top=dp[i-1][j];

                dp[i][j] = matrix[i][j] + min(top_left, top, top_right);
            }
        }
        int ans=Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            System.out.println(dp[m-1][i]);
            if(ans>dp[m-1][i]) ans=dp[m-1][i];
        }
        return ans;

    }
}