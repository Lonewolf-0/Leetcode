
public class Solution {
    public static int min(int a, int b){return Math.min(a,b);}
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int [][]dp = new int[n][n];

        for(int i=0; i<n; i++){
            for(int j=0; j<=i; j++){
                if(i==0 && j==0) {
                    dp[0][0] = triangle.get(0).get(0);
                    continue;
                }
                int top=Integer.MAX_VALUE;
                int top_left=Integer.MAX_VALUE;
                if(i>0){
                    if(j>0){
                        top_left=dp[i-1][j-1];
                    }
                    if(j<i){
                        top=dp[i-1][j];
                    }
                }
                dp[i][j] = triangle.get(i).get(j) + min(top, top_left);
            }
        }
        int min = Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            System.out.println(dp[n-1][i]);
            if(min>dp[n-1][i]) min=dp[n-1][i];
        }
        return min;
    }
}
