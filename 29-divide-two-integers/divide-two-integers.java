class Solution {
    public int divide(int dividend, int divisor) {
        int INT_MIN = Integer.MIN_VALUE, INT_MAX = Integer.MAX_VALUE;
        
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        
        boolean positive = (dividend >= 0) == (divisor >= 0);
        
        int a = (dividend > 0) ? -dividend : dividend;
        int b = (divisor > 0)  ? -divisor  : divisor;
        
        int quotient = 0;
        while (a <= b) {
            int current = b;
            int multiple = 1;
            while (current >= (INT_MIN >> 1) && a <= (current << 1)) {
                current <<= 1;
                multiple <<= 1;
            }
            a -= current;
            quotient += multiple;
        }
        
        return positive ? quotient : -quotient;
    }
}
