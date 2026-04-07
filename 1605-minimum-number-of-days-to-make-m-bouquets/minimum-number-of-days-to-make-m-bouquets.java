class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int n = bloomDay.length;

        if ((long) m * k > n)
            return -1;

        int low = 1, high = 0;

        for (int i : bloomDay) {
            if (i > high)
                high = i;
        }

        int ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isPossible(bloomDay, mid, m, k)) {
                ans = mid;
                high = mid - 1;
            } else
                low = mid + 1;
        }

        return ans;
    }

    public boolean isPossible(int[] bloomDay, int day, int m, int k) {
        int count = 0;
        int bouquets = 0;
        int n = bloomDay.length;

        for (int i = 0; i < n; i++) {
            if (bloomDay[i] <= day) {
                count++;
                if (count == k) {
                    bouquets++;
                    count = 0;
                }
            } else {
                count = 0;
                
                if ((m - bouquets) * k > n - i - 1)
                    break;
            }
            if (bouquets >= m)
                break;
        }
        return bouquets >= m;
    }
}