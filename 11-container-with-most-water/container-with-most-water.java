class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j = height.length-1;
        int area=0;
        int max_area=0;

        while(i<j){
            area = Math.min(height[i], height[j])*(j-i);
            max_area = Math.max(area, max_area);
            if(height[j]>height[i]) i++;
            else j--;
        }
        return max_area;


    }
}