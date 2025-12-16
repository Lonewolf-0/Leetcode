class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        for(int i=0; i<nums.length; i++){
			if(i==0){
				ans[i]=1;
			}			else{
				ans[i]=ans[i-1]*nums[i-1];
			}
		}
		int right=1;
		for(int i=nums.length-1; i>=0; i--){
						ans[i]=ans[i]*right;
						right=right*nums[i];
			}
            
        
		return ans;
            
        
    }
}