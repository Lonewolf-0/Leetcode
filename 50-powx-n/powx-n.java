class Solution {
    public double myPow(double x, int n) {
        if(n==-2147483648 && x>1) return 0;
        if(n<0) {
            x = 1/x;
            n= -n;
        }
        double result = 1;
        double current_product = x;

        while (n > 0) {
            if (n % 2 == 1)
                result = result * current_product;
            current_product = current_product * current_product;
            n = n / 2;
        }

        return result;
    }
}