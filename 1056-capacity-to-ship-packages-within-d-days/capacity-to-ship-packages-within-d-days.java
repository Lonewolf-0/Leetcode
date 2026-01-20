class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int start = 0;
        int end = 0;
        int res = Integer.MAX_VALUE;
        for (int w : weights) {
            start = Math.max(start, w); 
            end += w;                   
        }

        while(start<=end){
            int capacity = start + (end-start)/2;
            int d=1;
            int tmpSum=0;
            for(int weight: weights){
                if(tmpSum+weight>capacity){
                    tmpSum = weight;
                    d++;
                }
                else{
                    tmpSum+=weight;
                }
            }
            
            
            if(d<=days){
                res = capacity;
                end = capacity-1;
            }
            else{
                start = capacity+1;
            }
        }
        return res;
    }
}