class Solution {
    public List<Integer> findAnagrams(String s2, String s1) {
        int l1 = s1.length();
        int l2 = s2.length();
        if(l1>l2) return new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();
        for (int i = 0; i < l1; i++) {
            map1.put(s1.charAt(i), map1.getOrDefault(s1.charAt(i), 0) + 1);
        }
        for (int i = 0; i < l1; i++) {
            map2.put(s2.charAt(i), map2.getOrDefault(s2.charAt(i), 0) + 1);
        }
        for (int i = l1; i < l2; i++) {
            if (map1.equals(map2)) {
                ans.add(i - l1);
            }
            map2.put(s2.charAt(i), map2.getOrDefault(s2.charAt(i), 0) + 1);
            map2.put(s2.charAt(i - l1), map2.get(s2.charAt(i - l1)) - 1);
            map2.remove(s2.charAt(i - l1), 0);
        }
        if (map1.equals(map2)) {
            ans.add(l2 - l1);
        }
        return ans;
    }
}