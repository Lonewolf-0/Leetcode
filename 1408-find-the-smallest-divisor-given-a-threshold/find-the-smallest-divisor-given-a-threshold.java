class Solution {
    public int thresholdValue(int[] nums, int n){
        long sum=0;
        for(int i: nums){
            sum+=Math.ceil((double)i/n);
        }
        return (int) sum;
    }
    public int smallestDivisor(int[] nums, int threshold) {
        if (nums.length > threshold) return -1;
        int low = 1;
        int high = Arrays.stream(nums).max().getAsInt();

        while(low<=high){
            int mid = low+(high-low)/2;
            if(thresholdValue(nums, mid)<=threshold){
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }

        return low;

        
    }
}