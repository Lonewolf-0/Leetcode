class Solution {
    public int[] plusOne(int[] digits) {
        int carry=1;
        for(int i=digits.length-1; i>=0; i--){
            int tmp = carry;
            carry = (int)((digits[i]+carry)/10);
            digits[i] = (digits[i]+tmp)%10;
        }
        if(carry>0){
            //add carry at 0 index
            int []newArr = new int[digits.length+1];
            newArr[0] = carry;
            System.arraycopy(digits, 0, newArr,1 , digits.length);
            digits =  newArr;
        }
        
        return digits;


    }
}