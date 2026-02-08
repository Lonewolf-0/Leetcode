class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int ans=0;
        for(int i=0; i<nums.length;i++){
            maxHeap.offer(nums[i]);
        }
        for(int i=0; i<k; i++){
            ans = maxHeap.poll();
        }
        return ans;
    }
}