class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int start = 1;
        int end = Integer.MAX_VALUE;
        int res = Integer.MAX_VALUE;

        while(start<=end){
            int pileSize = start + (end-start)/2;
            int hours=0;
            for (int pile : piles) {
                hours += (int) Math.ceil((double) pile / pileSize);
            }
            
            
            if(hours<=h){
                res = Math.min(res,pileSize);
                end = pileSize-1;
            }
            else{
                start = pileSize+1;
            }
        }
        return res;
    
    }
}