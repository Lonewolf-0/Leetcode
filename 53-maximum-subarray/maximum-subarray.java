class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int temp_sum=0;
        int res=Integer.MIN_VALUE;

        for(int i=0; i<n; i++){
            temp_sum+=nums[i];
            res = Math.max(temp_sum, res);

            if(temp_sum<0) temp_sum=0;
        }
        return res;
    }
}