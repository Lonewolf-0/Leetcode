class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder res = new StringBuilder();
        int balance = 0;

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (currentChar == '(') {
                if (balance > 0) {
                    res.append(currentChar);
                }
                balance++;
            } else { 
                balance--;
                if (balance > 0) {
                    res.append(currentChar);
                }
            }
        }
        return res.toString();
    }
}